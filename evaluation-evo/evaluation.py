#!/usr/bin/env python3

# Created by Beda Berner
# beda.berner@hilti.com

from evo.core import metrics
from evo.core import lie_algebra as lie
from evo.tools.plot import *
import numpy as np

from evo.tools import plot
import matplotlib.pyplot as plt
import sys
from evo.tools.settings import SETTINGS

SETTINGS.plot_usetex = False
from evo.core import sync
from evo.tools import file_interface
import copy
from scipy.spatial.transform import Rotation as R
from evo.core.trajectory import PoseTrajectory3D


def traj_custom(ax: plt.Axes, plot_mode: PlotMode, traj: trajectory.PosePath3D,
                style: str = '-', color: str = 'black', label: str = "",
                alpha: float = 1.0, markers: str = 'None') -> None:
    """
    plot a path/trajectory based on xyz coordinates into an axis
    :param ax: the matplotlib axis
    :param plot_mode: PlotMode
    :param traj: trajectory.PosePath3D or trajectory.PoseTrajectory3D object
    :param style: matplotlib line style
    :param color: matplotlib color
    :param label: label (for legend)
    :param alpha: alpha value for transparency
    """
    x_idx, y_idx, z_idx = plot_mode_to_idx(plot_mode)
    x = traj.positions_xyz[:, x_idx]
    y = traj.positions_xyz[:, y_idx]
    if plot_mode == PlotMode.xyz:
        z = traj.positions_xyz[:, z_idx]
        ax.plot(x, y, z, linestyle=style, color=color, label=label, alpha=alpha, marker=markers)
        if SETTINGS.plot_xyz_realistic:
            set_aspect_equal_3d(ax)
    else:
        ax.plot(x, y, linestyle=style, color=color, label=label, alpha=alpha, marker=markers)
    if label:
        ax.legend(frameon=True)


def trajectories_custom(fig: plt.Figure, trajectories: typing.Union[
    trajectory.PosePath3D, typing.Sequence[trajectory.PosePath3D],
    typing.Dict[str, trajectory.PosePath3D]], plot_mode=PlotMode.xy,
                        title: str = "", subplot_arg: int = 111) -> None:
    """
    high-level function for plotting multiple trajectories
    :param fig: matplotlib figure
    :param trajectories: instance or container of PosePath3D or derived
    - if it's a dictionary, the keys (names) will be used as labels
    :param plot_mode: e.g. plot.PlotMode.xy
    :param title: optional plot title
    :param subplot_arg: optional matplotlib subplot ID if used as subplot
    """
    ax = prepare_axis(fig, plot_mode, subplot_arg)
    cmap_colors = None
    if SETTINGS.plot_multi_cmap.lower() != "none" and isinstance(
            trajectories, collections.Iterable):
        cmap = getattr(cm, SETTINGS.plot_multi_cmap)
        cmap_colors = iter(cmap(np.linspace(0, 1, len(trajectories))))

    # helper function
    def draw(t, name=""):
        if cmap_colors is None:
            color = next(ax._get_lines.prop_cycler)['color']
        else:
            color = next(cmap_colors)
        if SETTINGS.plot_usetex:
            name = name.replace("_", "\\_")
        if name != "evaluated estimate points":
            traj_custom(ax, plot_mode, t, '-', color, name)
        else:
            traj_custom(ax, plot_mode, t, 'dotted', color, name, markers='o')

    if isinstance(trajectories, trajectory.PosePath3D):
        draw(trajectories)
    elif isinstance(trajectories, dict):
        for name, t in trajectories.items():
            draw(t, name)
    else:
        for t in trajectories:
            draw(t)


if __name__ == "__main__":

    # check if files where provided in the command line argument
    if len(sys.argv) > 1:
        est_file = sys.argv[1]
        ref_file = sys.argv[2]
    else:
        # uncomment if hardcoded filepaths should be used
        # ref_file = 'path'
        # est_file = 'path'

        # comment if hardcoded filepaths should be used
        print('use: ./evaluation.py tum_est_file tum_ref_file')
        exit()

    traj_ref = file_interface.read_tum_trajectory_file(ref_file)

    apply_pole_tip_calibration = True
    # apply poletip calibration
    if apply_pole_tip_calibration == True:
        calibration_type = ref_file.split('_')[-1].lower()
        if calibration_type == 'pole.txt':
            # get the value by tf tf_echo /imu /pole_tip
            x=-0.009
            y=-0.015
            z=1.667
            # the values need to be inverted since we are interested in the distance pole_tip to imu (but in imu frame)
            calibration = np.array([[-x], [-y], [-z], [1]])


            # calibration = np.array([[0.0085], [-0.006], [-1.6847], [1]])
        elif calibration_type == 'prism.txt':
            # get the value by tf tf_echo /imu /prism
            x=--0.006
            y=-0.007
            z=0.273
            # the values need to be inverted since we are interested in the distance prism to imu (but in imu frame)
            calibration = np.array([[-x], [-y], [-z], [1]])
        elif calibration_type == 'imu.txt':
             calibration = np.array([[0], [0], [0], [1]])

        else:
            print("reference file has non supported calibration type. Please don't change the reference file names.")
            exit()
        data = np.genfromtxt(est_file, delimiter=' ', skip_header=False)
        stamps = data[:, 0]  # n x 1
        xyz = data[:, 1:4]  # n x 3
        quat = data[:, 4:]  # n x 4
        traj_est_no_cal = PoseTrajectory3D(xyz, quat, stamps)
        for i in range(data.shape[0]):
            rot_mat = R.from_quat([data[i, 4:8]]).as_matrix().reshape([3, 3])
            transl = data[i, 1:4].reshape([3, 1])
            homogeneous_transform = np.vstack([np.hstack([rot_mat, transl]), np.array([0, 0, 0, 1])])
            result = (homogeneous_transform @ (calibration))[:3].reshape([3, ])
            data[i, 1:4] = result

        stamps = data[:, 0]  # n x 1
        xyz = data[:, 1:4]  # n x 3
        quat = data[:, 4:]  # n x 4
        traj_est = PoseTrajectory3D(xyz, quat, stamps)

    else:
        traj_est = file_interface.read_tum_trajectory_file(est_file)

    # determine if a dense or sparse reference file is used
    if traj_ref.num_poses > 100:
        dense_trajectory = True
    else:
        dense_trajectory = False

    # timesync the reference and estimate trajectories
    max_diff = 1
    traj_ref_sync, traj_est_sync = sync.associate_trajectories(traj_ref, traj_est, max_diff)

    # align the trajectories
    traj_est_aligned = copy.deepcopy(traj_est_sync)
    umeyama_parameters = traj_est_aligned.align(traj_ref_sync, correct_scale=False, correct_only_scale=False)
    traj_est_aligned_complete = copy.deepcopy(traj_est)
    traj_est_aligned_complete.scale(umeyama_parameters[2])
    traj_est_aligned_complete.transform(lie.se3(umeyama_parameters[0], umeyama_parameters[1]))

    # calculate the metrics
    data = (traj_ref_sync, traj_est_aligned)
    ape_metric = metrics.APE(metrics.PoseRelation.translation_part)
    ape_metric.process_data(data)

    ape_stats = ape_metric.get_all_statistics()
    for i in ape_stats:
        print("APE {} = {}.".format(i, ape_stats[i]))

    # plot the trajectories
    fig = plt.figure()
    if dense_trajectory:
        traj_by_label = {
            "estimate": traj_est_aligned,
            "reference": traj_ref_sync
        }
        trajectories(fig, traj_by_label, plot.PlotMode.xyz)

    else:
        traj_by_label = {
            "estimate": traj_est_aligned_complete,
            "evaluated estimate points": traj_est_aligned,
            "reference": traj_ref_sync
        }
        trajectories_custom(fig, traj_by_label, plot.PlotMode.xyz)


    plt.show()

    seconds_from_start = [t - traj_est.timestamps[0] for t in traj_est_sync.timestamps]
    fig = plt.figure()

    # plot the error over time
    if dense_trajectory:
        plot.error_array(fig.gca(), ape_metric.error, x_array=seconds_from_start,
                         statistics={s: v for s, v in ape_stats.items() if s != "sse"},
                         name="APE", title="APE w.r.t. " + ape_metric.pose_relation.value, xlabel="$t$ (s)")
    else:
        plot.error_array(fig.gca(), ape_metric.error, x_array=seconds_from_start,
                         statistics={s: v for s, v in ape_stats.items() if s != "sse"},
                         name="APE", title="APE w.r.t. " + ape_metric.pose_relation.value, xlabel="$t$ (s)", marker='o',
                         linestyle='dotted')
    plt.show()
