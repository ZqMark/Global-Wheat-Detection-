#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/23 10:39
# @Author  : zyf
# @File    : new_hrnet_seg_train.py
# @Software: PyCharm
from paddlex.seg import transforms
import paddlex as pdx

train_transforms = transforms.Compose([
    transforms.RandomHorizontalFlip(prob=0.5),
    transforms.RandomVerticalFlip(prob=0.5),
    transforms.Normalize()
])
eval_transforms = transforms.Compose([
    transforms.Normalize()
])

train_dataset = pdx.datasets.SegDataset(
    data_dir='',
    file_list='data/train_list_new.txt',
    label_list='data/labels_new.txt',
    transforms=train_transforms,
    shuffle=True)
eval_dataset = pdx.datasets.SegDataset(
    data_dir='',
    file_list='data/val_list_new.txt',
    label_list='data/labels_new.txt',
    transforms=eval_transforms)

num_classes = len(train_dataset.labels)
print(num_classes)
model = pdx.seg.HRNet(
    num_classes=num_classes
)
model.train(
    num_epochs=120,
    train_dataset=train_dataset,
    train_batch_size=32,
    eval_dataset=eval_dataset,
    learning_rate=0.01,
    log_interval_steps=100,
    save_interval_epochs=10,
    save_dir='output/hrnet_1023',
    pretrain_weights='output/pre',
    use_vdl=True)