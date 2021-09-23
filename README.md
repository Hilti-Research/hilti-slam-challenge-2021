# The HILTI SLAM Challenge

<p align="center">
  <img src="https://github.com/hemi86/hiltislamchallenge/blob/be56ed92d5415dff49e53b58bbeab019f923f883/images/HILTI_SLAM_CHALLENGE_VISUAL.jpg"  width="70%"  alt="HILTI SLAM Challeng"/>
</p>


This is the Github repository for the SLAM challenge hosted at https://www.hilti-challenge.com/. The main purpose of the repository is to allow easy discussion and the reporting of issues.

## Description
The participants are required to run their SLAM algorithms on sequences from the HILTI-Challenge Dataset, which includes images, IMU measurements, and LIDAR data recorded with a custom handheld device. The goal is to estimate the position of the handheld device as accurately as possible, utilizing any desired sensor combinations. The winner will be selected based on the accuracy of the estimated trajectories and will be awarded 7,000 USD and will also be invited to present their approach at the IROS 2021 Workshop [Perception and Navigation for Autonomous Robotics in Unstructured and Dynamic Environments](https://iros2021-pnarude.github.io/) taking place on September 27th, 2021 in Prague. The second and third ranked teams will be awared  2,000 USD and 1,000 USD repectively. Only participants affiliated with educational institutions (Students, Postdocs) are eligible to win the cash prize.

## Deadline

The **deadline to submit the estimated trajectories and report is Sept 25th 2021 23:59:59 UTC!**

## Evaluation Metric
The submission will be ranked based on the completeness and accuracy of the estimated trajectories. 

## Hardware

Our sensor suite consists of a Sevensense Alphasense camera head, an Ouster OS0-64, a Livox MID70 and an ADIS16445 IMU. The sensors are mounted on a surveying pole for handheld operation. The syncronization between the sensors is done by a FPGA for the cameras and the ADIS16445 IMU. The cameras and the LIDARs are syncronized via PTP. The time between all sensors is aligned to within 1 ms.

## Datasets

please visit https://www.hilti-challenge.com/dataset.html.

## Submission Format
Each participant should submit the estimated trajectories for the above datasets and a report describing the adopted method. Send your results to [Email](mailto:michael.helmberger@hilti.com?subject=[HILTI%20SLAM%20Challenge]%20Submission%20Team). **Submissions are not automatically published** – you can review the results and decide whether to publish by yourself. Submissions can also be withdrawn completely.

### Estimated Trajectories
The estimated trajectories should be stored in plain text files in the following format:

    # timestamp_s tx ty tz qx qy qz qw
    1.403636580013555527e+09 0.0 0.0 0.0 0.0 0.0 0.0 0.0
    …… 

The file names should be the same as the names of the bag/zip. For example, the result for “seq1.bag” should be saved as “seq1.txt”. The file should be space separated. Each line stands for the pose at the specified timestamp. The timestamps are in the unit of second and used to establish temporal correspondences with the groundtruth. 

The pose is composed of translation (`tx` `ty` `tz`, in meters) and quaternion (in Hamilton quaternion, the `w` component is at the end). The pose should specify the pose of the IMU in the world frame. For example, after converting the pose to a transformation matrix `Twi`, one should be able to transform the homogeneous point coordinates in IMU frame to world frame as `pw = Twi * pi`.

### Report
In addition to the estimated trajectories, the participants are required to submit a short report summarizing their approach.
The reports of all teams will be published on the website after the competition.
The format of the report is left to the discretion of the participants, however the report must specify the following information:
* A brief overview of the approach:
  * Filter or optimization-based (or else)?
  * Is the method causal? (i.e. does not use information from the future to predict the pose at a given time).
  * Is bundle adjustment (BA) used? What type of BA, e.g. full BA or sliding window BA?
  * Is loop closing used?
* Exact sensor modalities used (IMU, stereo or mono, LIDAR?)
* Total processing time for each sequence and the used hardware
* Whether the same set of parameters is used throughout all the sequences

The participants are welcome to include further details of their approach, eventual references to a paper describing the approach, or any other additional information.

## Questions

If you have a question about the challenge, please file a Github issue in this repository. This way the question and response will be visible to everyone.
Subscribe to [this issue](https://github.com/hemi86/hiltislamchallenge/issues/1) to get notified about changes to this document.

## Acknowledgement

We would like to thank to thank Danwei Wang, Christian Laugier, Philippe Martinet, Yufeng Yue for hosting our challenge at the IROS2021 workshop “Perception and Navigation for Autonomous Robotics in Unstructured and Dynamic Environments”. Futher, we thank Prof. Davide Scaramuzza and Giovanni Coffi for the great support in organizing the challenge, verifying the data and providing the [UZH FPV Challenge](https://fpv.ifi.uzh.ch/) as template for this challenge.


## License

All datasets and benchmarks on this page are copyright by us and published under the [Creative Commons Attribution-NonCommercial-ShareAlike 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/) License. This means that you must attribute the work in the manner specified by the authors, you may not use this work for commercial purposes and if you alter, transform, or build upon this work, you may distribute the resulting work only under the same license.


