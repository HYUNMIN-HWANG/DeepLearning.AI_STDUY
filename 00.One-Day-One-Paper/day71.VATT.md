# VATT: Transformers for Multimodal Self-Supervised Learning from Raw Video, Audio and Text

### **Video Audio-Text Transformer (VATT)**
- a framework for learning multimodal representations from unlabeled data using convolution-free Transformer architectures
- takes raw signals as inputs and extracts multi-modal representations that are rich enough to benefit a variety of downstream tasks
- self-supervised, multimodal pre-training of three Transformers
- sharing weights among the video, audio, and text modalities
- DropToken : effective technique to reduce the training complexity with a minor reduction of the end Transformers’ performance.    
    - randomly sample a portion of the tokens
    - then, feed the sampled sequence, not the complete set of tokens, to the Transformer
    - better to keep a high-fidelity input and randomly sample the tokens via DropToken

### **convolution-free VATT architecture**
![image](https://user-images.githubusercontent.com/70581043/154843418-f3cdd6fa-c715-40d9-8d1e-ec629f06c89f.png)
1. feed each modality to a tokenization layer (the raw input is projected to an embedding vector followed by a Transformer)
    - raw signals :  3-channel RGB pixels of video / form of air density amplitudes (waveforms) / sequence of words
2. the backbone extracts modality-specific representations, which are then mapped to common spaces to be compared with each other by contrastive losses
     1) The backbone Transformers are separate and have specific weights for each modality
     2) The Transformers share weights, namely, there is a single backbone Transformer applied to any of the modalities
    - Common Space Projection ; enables us to directly compare video-audio pairs as well as video-text pairs by the cosine similarity 
![image](https://user-images.githubusercontent.com/70581043/154843848-bdf98c80-8d2c-4886-a68a-f1d4244bb027.png)
    -  Multimodal Contrastive Learning ; Noise Contrastive Estimation (NCE) + video-audio pairs and Multiple Instance Learning NCE (MIL-NCE) 
![image](https://user-images.githubusercontent.com/70581043/154843934-7947bcf9-8909-428b-9b4d-7e0b5adfff54.png)


### Limitation
- not all videos have organic audio or speech, while our approach depends on meaningful multimodal correspondences.
- the text modality currently consists of speech transcripts, which are noisy and sometimes sparse
- our method is still demanding in computation