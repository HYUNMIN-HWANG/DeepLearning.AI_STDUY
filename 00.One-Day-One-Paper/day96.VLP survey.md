# VLP : A Survey on Vision-Language Pre-training

## Feature extraction
1. Image Feature Extraction
    -  OD-based Region Features (OD-RFs) : object detection, Fast RCNN
    - CNN-based Grid Features (CNN-GFs) : ResNet
    - ViT-based Patch Features (ViT-PFs) : ViT, DeiT
2. Video Feature Extraction
    - CNN-GFs or ViT-PFs 사용 
3. Text Feature Extraction
    - BERT, segment the input sentence into a sequence of subwords 

## Model architecture
![image](https://user-images.githubusercontent.com/70581043/168975356-ce5b8614-1489-486c-a3ff-1667796d5847.png)
1. Single-stream : The single-stream architecture refers to that the text and visual features are concatenated together, then fed into a single transformer block
2. Dual-stream : The dual-stream architecture refers to that the text and visual features are not concatenated together but sent to two different transformer blocks independently, do not share parameters, 

## Pre-training objectives
1) Completion : Masked Language Modeling, Prefix Language Modeling, Masked Vision Modeling
2) Matching : Vision-Language Matching, Vision-Language Matching, Word-Region Alignment
3) Temporal : Frame Order Modeling
4) Particular Pre-training Objects

## Pre-training datasets
![image](https://user-images.githubusercontent.com/70581043/168975681-0d8bba90-3ba4-4087-b028-8b9884099c88.png)

## Downstream tasks
1. Classification : Visual Question Answering (VQA), Visual Reasoning and Compositional Question Answering (GQA), Video-Language Inference (VLI), Natural Language for Visual Reasoning (NLVR), Visual Entailment (VE), Visual Commonsense Reasoning (VCR), Grounding Referring Expressions (GRE), Category Recognition (CR)
2. Regression : Multi-modal Sentiment Analysis (MSA)
3. Retrieval : Vision-Language Retrieval (VLR)
4. Generation : Visual Captioning (VC), Novel Object Captioning at Scale (NoCaps), Visual Dialogue (VD)
5. 그 외 : Multi-modal Machine Translation (MMT), Vision-Language Navigation (VLN), Optical Character Recognition (OCR)

## SOTA VLP models
![image](https://user-images.githubusercontent.com/70581043/168976205-92f29ca0-2951-430d-bbf3-e89b5407ded6.png)

## New Frontiers
- Acousitc 데이터의 활용
- large-scale dataset을 사용해야 한다는 한계
- Prompt tuning 을 활용해서 parameter inefficiency 문제를 해결 -> computation cost를 줄일 수 있고, pre-training과 fine-tuning 사이의 gap차이를 줄일 수 있다. 