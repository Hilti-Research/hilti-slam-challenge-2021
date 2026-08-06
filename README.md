# The Hilti SLAM Challenge

<p align="center">
  <a href="https://huggingface.co/datasets/Hilti-Research/slam-challenge-2021"><img src="https://img.shields.io/badge/🤗%20Hugging%20Face-Dataset-yellow" alt="Hugging Face Dataset"/></a>
  <a href="https://arxiv.org/abs/2109.11316"><img src="https://img.shields.io/badge/arXiv-2109.11316-b31b1b" alt="arXiv"/></a>
  <a href="https://www.hilti-challenge.com/"><img src="https://img.shields.io/badge/Webpage-hilti--challenge.com-blue" alt="Webpage"/></a>
</p>

<p align="center">
  <img src="https://github.com/hemi86/hiltislamchallenge/blob/be56ed92d5415dff49e53b58bbeab019f923f883/images/HILTI_SLAM_CHALLENGE_VISUAL.jpg"  width="70%"  alt="HILTI SLAM Challeng"/>
</p>


This is the Github repository for the SLAM challenge hosted at https://www.hilti-challenge.com/. The main purpose of the repository is to allow easy discussion and the reporting of issues.

## Description
The participants are required to run their SLAM algorithms on sequences from the HILTI-Challenge Dataset, which includes images, IMU measurements, and LIDAR data recorded with a custom handheld device. The goal is to estimate the position of the handheld device as accurately as possible, utilizing any desired sensor combinations. The winner will be selected based on the accuracy of the estimated trajectories and will be awarded 7,000 USD and will also be invited to present their approach at the IROS 2021 Workshop [Perception and Navigation for Autonomous Robotics in Unstructured and Dynamic Environments](https://iros2021-pnarude.github.io/) taking place on September 27th, 2021 in Prague. The second and third ranked teams will be awared  2,000 USD and 1,000 USD repectively. Only participants affiliated with educational institutions (Students, Postdocs) are eligible to win the cash prize.

## Winners

Please visit https://www.hilti-challenge.com/ for the leaderboard.

## Datasets

The datasets along with the corresponding ground truth sequences can be downloaded [here](https://huggingface.co/datasets/Hilti-Research/slam-challenge-2021).

## Publication

When using this work in an academic context, please cite the following publication:

```bibtex
@ARTICLE{hiltislamchallenge2021,
  author={Helmberger, Michael and Morin, Kristian and Berner, Beda and Kumar, Nitish and Cioffi, Giovanni and Scaramuzza, Davide},
  journal={IEEE Robotics and Automation Letters}, 
  title={The Hilti SLAM Challenge Dataset}, 
  year={2022},
  volume={7},
  number={3},
  pages={7518-7525},
  doi={10.1109/LRA.2022.3183759}}
```

## Acknowledgement

We would like to thank to thank Danwei Wang, Christian Laugier, Philippe Martinet, Yufeng Yue for hosting our challenge at the IROS2021 workshop “Perception and Navigation for Autonomous Robotics in Unstructured and Dynamic Environments”. Futher, we thank Prof. Davide Scaramuzza and Giovanni Coffi for the great support in organizing the challenge, verifying the data and providing the [UZH FPV Challenge](https://fpv.ifi.uzh.ch/) as template for this challenge.


## License

All datasets and benchmarks on this page are copyright by us and published under the [Creative Commons Attribution-NonCommercial-ShareAlike 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/) License. This means that you must attribute the work in the manner specified by the authors, you may not use this work for commercial purposes and if you alter, transform, or build upon this work, you may distribute the resulting work only under the same license.


