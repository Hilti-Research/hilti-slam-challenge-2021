# HILTI SLAM Challenge

This is the Github repository for the SLAM challenge hosted at https://www.hilti-challenge.com/. The main purpose of the repository is to allow easy discussion and the reporting of issues.

<p align="center">
  <img src="https://github.com/hemi86/hiltislamchallenge/blob/8f5f9a71e0bfd1fb44f1b6a0eb169fff44c23383/images/HILTI_SLAM_CHALLENGE_VISUAL.jpg?raw=true" alt="HILTI SLAM Challeng"/>
</p>

## Description
The participants are required to run their SLAM algorithms on sequences from the HILTI-Challenge Dataset, which includes images, IMU measurements, and LIDAR data recorded with a custom handheld device. The goal is to estimate the position of the handheld device as accurately as possible, utilizing any desired sensor combinations. The winner will be selected based on the accuracy of the estimated trajectories and will be awarded 7,000 USD and will also be invited to present his approach at the IROS 2021 Workshop "Perception and Navigation for Autonomous Robotics in Unstructured and Dynamic Environments" taking place on September 27th, 2021 in Prague. The second and third ranked teams will be awared  2,000 USD and 1,000 USD repectively. Only participants affiliated with educational institutions
(Students, Postdocs, etc) are eligible to win the cash prize.

## Deadline

The **deadline to submit the estimated trajectories and report is September 25, 2021**

## Evaluation Metric
The submission will be ranked based on the accuracy. A python script for self-evaluation will be provided here soon.

## Datasets

[Coming soon]

## Submission Format
Each participant should submit the estimated trajectories for the above datasets and a report describing the adopted method. Send your results to [Michael Helmberger](mailto:michael.helmberger@hilti.com?subject=[HILTI%20SLAM%20Challenge]%20Submission%20Team). **Submissions are not automatically published** – you can review the results and decide whether to publish by yourself. Submissions can also be withdrawn completely.

### Estimated Trajectories
The estimated trajectories should be stored in plain text files in the following format:

    # timestamp tx ty tz qx qy qz qw
    1.403636580013555527e+09 0.0 0.0 0.0 0.0 0.0 0.0 0.0
    …… 

The file names should be the same as the names of the bag/zip. For example, the result for “seq1.bag” should be saved as “seq1.txt”. The file should be space separated. Each line stands for the pose at the specified timestamp. The timestamps are in the unit of second and used to establish temporal correspondences with the groundtruth. 

The pose is composed of translation (`tx` `ty` `tz`, in meters) and quaternion (in Hamilton quaternion, the `w` component is at the end). The pose should specify the pose of the IMU in the world frame. For example, after converting the pose to a transformation matrix `Twi`, one should be able to transform the homogeneous point coordinates in IMU frame to world frame as `pw = Twi * pi`.

### Report
In addition to the estimated trajectories, the participants are required to submit a short report (maximum **4** pages, 10MB, pdf) summarizing their approach.
The reports of all teams will be published on the website after the competition.
The format of the report is left to the discretion of the participants, however the report must specify the following information:
* A brief overview of the approach:
  * Filter or optimization-based (or else)?
  * Is the method causal? (i.e. does not use information from the future to predict the pose at a given time).
  * Is bundle adjustment (BA) used? What type of BA, e.g. full BA or sliding window BA?
  * Is loop closing used?
* Exact sensor modalities used (IMU, stereo or mono, LIDAR?)
* Total processing time for each sequence
* Exact specifications of the hardware used
* Whether the same set of parameters is used throughout all the sequences

The participants are welcome to include further details of their approach, eventual references to a paper describing the approach, or any other additional information.

## Questions

If you have a question about the challenge, please file a Github issue in this repository. This way the question and response will be visible to everyone.
Subscribe to [this issue](https://github.com/hemi86/hiltislamchallenge/issues/1) to get notified about changes to this document.

## Acknowledgement

We would like to thank to thank Danwei Wang, Christian Laugier, Philippe Martinet, Yufeng Yue for hosting our challenge at the IROS2021 workshop “Perception and Navigation for Autonomous Robotics in Unstructured and Dynamic Environments”. Futher, we thank Prof. Davide Scaramuzza and Giovanni Coffi for the great support in organizing the challenge, verifying the data and providing the [UZH FPV Challenge](https://fpv.ifi.uzh.ch/) as template for this challenge.



