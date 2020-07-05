# HM_DataAug (Team name: opossum)
Histogram Matching for Domain Adaptation: Solution to M\&Ms 2020

> The authors of this paper declare that the segmentation method they implemented for participation in the M&Ms challenge has not used any pre-trained models nor additional MRI datasets other than those provided by the organizers.

## Prepare data

- Clone this repo. and put testing cases in `mnms`

- Copy and rename the the end-diastole (ED) and end-systole (ES) phases data to a single folder `test_data`, by running

> python prepare_data.py

## Prepare Trained Models and code

- Download trained models and put them in `V2_nnUNet/nnUNet/nnunet`

- Install [nnUNet](https://github.com/MIC-DKFZ/nnunet)

    > cd V2_nnUNet/nnUNet

    > pip install -e .

    > cd nnunet

> Please use our modified nnUNet in this repo. rather than the official nnUNet.

**All the following commands should be run in V2_nnUNet/nnUNet/nnunet**

## Solution 1: 3D Best Model

Run

```python
nnUNet_predict -i ../../../mnms/test_data -o ../../../mnms/solution1_output -m 3d_fullres -t Task601_BestHMAug --save_npz
```

Segmentation Results will be in `HM_DataAug/mnms/solution1_output`.


## Solution 2: 3D Final Model

```python
nnUNet_predict -i ../../../mnms/test_data -o ../../../mnms/solution2_output -m 3d_fullres -t Task602_HMAugMMS --save_npz
```

Segmentation Results will be in `HM_DataAug/mnms/solution2_output`.

## Solution 3: 2D-3D Best Model Ensemble

```python
nnUNet_predict -i ../../../mnms/test_data -o ../../../mnms/temp_solution3 -m 2d -t Task601_BestHMAug --save_npz

nnUNet_ensemble -f ../../../mnms/solution1_output ../../../mnms/temp_solution3 -o ../../../mnms/solution3_output
```

Segmentation Results will be in `HM_DataAug/mnms/solution3_output`.

## Solution 4: 2D-3D Final Model Ensemble

```python
nnUNet_predict -i ../../../mnms/test_data -o ../../../mnms/temp_solution4 -m 2d -t Task602_HMAugMMS --save_npz

nnUNet_ensemble -f ../../../mnms/solution2_output ../../../mnms/temp_solution4 -o ../../../mnms/solution4_output
```
Segmentation Results will be in `HM_DataAug/mnms/solution4_output`.

## Solution 5: 2D-3D All Model Ensemble

```python
nnUNet_ensemble -f ../../../mnms/solution1_output ../../../mnms/solution2_output ../../../mnms/temp_solution3 ../../../mnms/temp_solution4 -o ../../../mnms/solution5_output
```

Segmentation Results will be in `HM_DataAug/mnms/solution5_output`.

## Clean Results

- cd ../../../mnms
- rm -rf temp*
- rm solution1_output/*.npz
- rm solution1_output/*.pkl
- rm solution2_output/*.npz
- rm solution2_output/*.pkl
