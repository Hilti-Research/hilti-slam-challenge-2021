# Evaluation of the HILTI Challenge data

The evaluation is based on [evo](https://github.com/MichaelGrupp/evo) and uses SE3 alignment to compute the absolute trajectory error (ATE). We also provide example data from [SVO2.0](http://rpg.ifi.uzh.ch/svo2.html) and [hdl_graph_slam](https://github.com/koide3/hdl_graph_slam).

## Dependencies
To run the evaluation script Python >= 3.7 is required.

The required dependencies can be installed with the following command:
```
pip3 install -r requirements.txt
```
The estimated trajectory can then be evaluated

```
./evaluation.py <estimation_tum> <reference_tum>
```
where all trajectories have to be provided in the TUM format 
```
# timestamp_s tx ty tz qx qy qz qw
1.403636580013555527e+09 0.0 0.0 0.0 0.0 0.0 0.0 0.0
…… 
```
Names of the provided reference files should not be changed as they indicate which frame the reference is in.
