# Computer Vision and Medical Imaging AI

## Overview

This domain covers perception AI for healthcare — the ability to extract clinical insights from visual and audio data. It spans medical image analysis (radiology, pathology, dermatology), DICOM pipeline integration for AI inference, wound assessment, document OCR, medication verification, surgical workflow recognition, and audio perception (respiratory/heart sounds, conversation analysis, fall detection). For fullstack healthcare engineers, mastery means understanding how to build, integrate, and deploy computer vision and audio AI models within clinical workflows while meeting FDA SaMD requirements.

**Connections to prior domains:**
- Builds on ML Fundamentals (D-2) — CNNs, transfer learning, evaluation metrics
- Extends Predictive AI (D-3) — classification and regression applied to image/audio data
- Leverages Foundation Models (D-4) — vision transformers, multimodal models
- Connects to Regulatory Landscape (D-1) — FDA SaMD/SiMD pathways critical here

**Prerequisites for later domains:**
- Fine-Tuning (D-8) — medical imaging is a primary use case for domain adaptation
- Clinical Decision Support (D-9) — imaging AI outputs feed decisioning systems
- AI Safety (D-10) — imaging AI requires rigorous clinical evaluation
- Agentic Systems (D-12) — multimodal perception is a core agent capability

---

## Key Concepts

### 1. Medical Imaging Fundamentals

**DICOM Standard (Digital Imaging and Communications in Medicine)**
The universal standard for storing, transmitting, and displaying medical images. DICOM files contain both pixel data and rich metadata (patient demographics, acquisition parameters, study/series hierarchy). Understanding DICOM is non-negotiable for healthcare imaging AI.

**Medical Imaging Modalities**
Each modality produces distinct data characteristics requiring different AI approaches:
- **X-ray/Radiography** — 2D projection images; chest X-rays are the most common imaging study
- **CT (Computed Tomography)** — 3D volumetric data from X-ray cross-sections
- **MRI (Magnetic Resonance Imaging)** — 3D/4D soft tissue imaging with multiple sequences (T1, T2, FLAIR)
- **Ultrasound** — Real-time, portable, operator-dependent imaging
- **Mammography** — Specialized X-ray for breast tissue
- **PET/SPECT** — Nuclear medicine functional imaging
- **Fundoscopy** — Retinal imaging for ophthalmology

**PACS (Picture Archiving and Communication System)**
Enterprise system for storing and retrieving medical images. AI systems must integrate with PACS via DICOM send/receive or DICOMweb APIs.

**DICOMweb**
RESTful API standard for accessing DICOM data over HTTP (WADO-RS, STOW-RS, QIDO-RS). Critical for modern web-based AI integrations.

### 2. Computer Vision Architectures for Medical Imaging

**Convolutional Neural Networks (CNNs)**
The foundational architecture for medical image analysis. Key variants:
- **ResNet** — Residual connections enabling very deep networks; widely used as backbone
- **DenseNet** — Dense connections for feature reuse; popular for chest X-ray analysis (CheXNet)
- **EfficientNet** — Balanced scaling of depth/width/resolution
- **Inception** — Multi-scale feature extraction

**Vision Transformers (ViT)**
Attention-based architectures increasingly used in medical imaging. Self-attention captures long-range dependencies useful for pathology and radiology.

**U-Net and Segmentation Architectures**
The dominant architecture for medical image segmentation:
- **U-Net** — Encoder-decoder with skip connections; the workhorse of medical segmentation
- **V-Net** — 3D extension of U-Net for volumetric data
- **nnU-Net** — Self-configuring U-Net that automatically adapts to any medical segmentation task
- **UNETR** — Transformer-based encoder with U-Net decoder for 3D segmentation
- **Swin UNETR** — Shifted window transformer for efficient 3D medical image segmentation

**Object Detection in Medical Imaging**
Detecting and localizing abnormalities:
- **YOLO variants** — Real-time detection for screening applications
- **Faster R-CNN** — Two-stage detection for precise localization
- **RetinaNet** — Focal loss for handling class imbalance common in medical data

### 3. Clinical Application Areas

**Radiology AI**
- Chest X-ray interpretation (pneumonia, cardiomegaly, nodules, fractures)
- CT analysis (pulmonary embolism, stroke, lung nodule characterization)
- MRI analysis (brain tumors, knee injuries, cardiac function)
- Automated triage and prioritization of critical findings
- Quantitative measurements (tumor volumetry, bone density)

**Digital Pathology and Computational Pathology**
- Whole Slide Imaging (WSI) — gigapixel images requiring specialized handling
- Multiple Instance Learning (MIL) — weakly supervised learning for WSI without pixel-level annotations
- Tissue classification, cell counting, mitotic figure detection
- Cancer grading (Gleason scoring for prostate, HER2 for breast)
- Tools: QuPath, PathML, Digital Slide Archive

**Dermatology AI**
- Skin lesion classification (melanoma vs. benign nevi)
- Dermoscopic image analysis
- Skin condition recognition from smartphone photos
- Key dataset: ISIC (International Skin Imaging Collaboration) Archive

**Wound Assessment**
- Automated wound measurement (area, depth, perimeter)
- Tissue type classification (granulation, necrotic, slough)
- Healing trajectory prediction
- Remote wound monitoring via smartphone cameras

**Ophthalmology AI**
- Diabetic retinopathy screening from fundus images
- Glaucoma detection from OCT scans
- Age-related macular degeneration assessment

**Document OCR for Healthcare**
- Medical document digitization and extraction
- Prescription reading and medication verification
- Insurance card and ID scanning
- Handwritten clinical note recognition

**Surgical Workflow Recognition**
- Surgical phase recognition from video
- Tool detection and tracking
- Anomaly detection during procedures
- Training and quality assessment applications

### 4. DICOM Pipeline Integration for AI Inference

**AI Integration Architecture Patterns**

*Pattern 1: DICOM Router (Inline)*
Imaging modality → PACS → DICOM Router → AI Service → Results back to PACS
- Orthanc configured to auto-route studies matching criteria to AI
- Results stored as DICOM SEG, SR, or Secondary Capture objects

*Pattern 2: DICOMweb Pull (Event-driven)*
PACS publishes events → AI service polls/subscribes → Pulls study via DICOMweb → Processes → Pushes results via STOW-RS
- More decoupled; works with cloud-based AI services

*Pattern 3: Worklist-based*
AI workitem created → AI service claims workitem → Processes → Completes workitem with results
- IHE AI Workflow for Imaging (AIW-I) profile
- DICOM Supplement 251 for AI inference requests

**Key Tools and Libraries**

- **pydicom** — Python library for reading/writing DICOM files, extracting pixel data as NumPy arrays
- **highdicom** — High-level Python API for creating DICOM SEG objects, Structured Reports, and other complex DICOM types from AI outputs
- **Orthanc** — Lightweight open-source DICOM server with REST API and plugin system
- **OHIF Viewer** — Open-source web-based medical image viewer for displaying original images and AI results
- **dcm4chee** — Enterprise-grade open-source PACS
- **DICOMweb Client** — Libraries for WADO-RS, STOW-RS, QIDO-RS

**AI Output DICOM Encoding**
- **DICOM Segmentation (SEG)** — Pixel-wise segmentation masks stored as DICOM objects
- **DICOM Structured Report (SR)** — Coded findings, measurements, and observations
- **DICOM Secondary Capture (SC)** — Annotated images (heatmaps, bounding boxes)
- **DICOM Parametric Map** — Voxel-wise quantitative measurements
- **DICOM Presentation State (PR)** — Overlay annotations on original images

### 5. FDA SaMD Requirements for Diagnostic Imaging AI

**Regulatory Classification**
- **SaMD (Software as a Medical Device)** — Software intended for medical purposes without being part of a hardware device
- **SiMD (Software in a Medical Device)** — Software that is part of a medical device
- Most imaging AI is classified as SaMD

**Risk Classification (IMDRF Framework)**
Based on the significance of the information provided by the SaMD to the healthcare decision and the state of the healthcare situation:
- **Class I (Low Risk)** — Informational, non-critical
- **Class II (Moderate Risk)** — Most imaging AI falls here (computer-aided detection/diagnosis assisting clinicians)
- **Class III (High Risk)** — Autonomous diagnostic decisions, life-critical situations

**Regulatory Pathways**
- **510(k) Clearance** — ~97% of imaging AI devices; must demonstrate "substantial equivalence" to a predicate device already on the market
- **De Novo Classification** — For novel devices with no predicate; ~3% of AI devices; creates a new device classification that others can reference
- **PMA (Premarket Approval)** — Highest risk devices; rare for imaging AI

**Key FDA Guidance Documents**
- Predetermined Change Control Plan (PCCP) — Allows pre-specified algorithm updates without new submissions (finalized August 2025)
- Good Machine Learning Practice (GMLP) — 10 guiding principles for ML device development (October 2021)
- AI/ML SaMD Action Plan (January 2021) — Overall FDA strategy
- Lifecycle Management guidance (January 2025 draft) — Marketing submission recommendations

**Clinical Validation Requirements**
- Multi-Reader Multi-Case (MRMC) studies — Standard for diagnostic imaging AI
- Standalone performance testing (sensitivity, specificity, AUC)
- Real-world performance data collection
- Subgroup analysis for demographic fairness
- Labeling requirements: must indicate ML use, PCCP status, and implemented changes

**FDA-Cleared AI Devices Database**
The FDA maintains a public list of AI/ML-enabled medical devices: https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-aiml-enabled-medical-devices

### 6. Audio Perception for Clinical Sounds

**Cardiac Auscultation AI**
- Phonocardiogram (PCG) analysis — recording and classifying heart sounds (S1, S2, murmurs, gallops)
- Heart sound classification: normal vs. abnormal, murmur detection and grading
- Architectures: CNNs on spectrograms, LSTM/RNN on temporal features, CNN-LSTM hybrids
- Key dataset: PhysioNet/CinC Challenge 2016 (heart sound classification), PhysioNet Challenge 2022 (murmur detection)

**Respiratory Sound Analysis**
- Lung sound classification: normal breathing, crackles, wheezes, stridor
- Disease detection: COPD, asthma, pneumonia, COVID-19
- Digital stethoscope integration for objective analysis
- Key dataset: ICBHI 2017 Respiratory Sound Database (5.5 hours, 6898 cycles, 126 subjects)

**Audio Feature Extraction**
- Mel-Frequency Cepstral Coefficients (MFCCs) — standard audio features
- Mel spectrograms — time-frequency representation
- Short-Time Fourier Transform (STFT)
- Wavelet transforms for multi-resolution analysis
- Chromagrams for tonal analysis

**Other Clinical Audio Applications**
- Fall detection from ambient audio
- Patient distress detection (coughing, moaning, calling for help)
- Conversation analysis for clinical documentation
- Sleep apnea detection from breathing sounds
- Swallowing sound analysis for dysphagia screening

### 7. Medical Imaging Datasets and Benchmarks

**Chest X-ray Datasets**
- **NIH ChestX-ray14** — 112,120 frontal X-rays, 14 disease labels, 30,805 patients (https://www.kaggle.com/datasets/nih-chest-xrays/data)
- **CheXpert** — 224,316 chest radiographs from Stanford, uncertainty labels (https://stanfordmlgroup.github.io/competitions/chexpert/)
- **MIMIC-CXR** — 377,110 images in DICOM format with radiology reports (https://physionet.org/content/mimic-cxr/2.1.0/)
- **PadChest** — 160,000+ images with 174 radiographic findings

**Multi-organ and Segmentation**
- **Medical Segmentation Decathlon** — 10 tasks across organs and modalities (http://medicaldecathlon.com/)
- **AMOS** — Abdominal Multi-Organ Segmentation (CT and MRI)
- **TotalSegmentator** — 1,228 CT images with 117 anatomical structures

**Pathology Datasets**
- **CAMELYON16/17** — Breast cancer metastasis detection in lymph node WSIs
- **TCGA (The Cancer Genome Atlas)** — Multi-cancer genomic and imaging data via TCIA

**Other Key Datasets**
- **ISIC Archive** — Skin lesion images for dermatology (https://www.isic-archive.com/)
- **The Cancer Imaging Archive (TCIA)** — Large cancer imaging collections (https://www.cancerimagingarchive.net/)
- **RSNA AI Challenges** — Competition datasets for various tasks (https://www.rsna.org/artificial-intelligence/data)
- **OpenNeuro** — Neuroimaging data repository (https://openneuro.org/)

### 8. Frameworks and Tools

**MONAI (Medical Open Network for AI)**
PyTorch-based framework specifically for medical imaging AI. Includes:
- **MONAI Core** — Transforms, data loaders, architectures (U-Net, UNETR, etc.), loss functions (Dice), metrics
- **MONAI Label** — Interactive annotation tool with AI-assisted labeling
- **MONAI Deploy** — Packaging and deployment of medical imaging AI applications
- **MONAI Bundle** — Standardized model packaging format

**Other Frameworks**
- **TorchIO** — PyTorch library for 3D medical image preprocessing and augmentation
- **SimpleITK** — Simplified interface to ITK for image registration and filtering
- **OpenCV** — General computer vision (preprocessing, augmentation)
- **Albumentations** — Fast image augmentation library
- **librosa** — Audio analysis library for clinical sound processing

**Annotation Tools**
- **3D Slicer** — Open-source platform for medical image visualization and annotation
- **ITK-SNAP** — Interactive segmentation of 3D medical images
- **CVAT** — Computer Vision Annotation Tool (general purpose, adaptable to medical)
- **MONAI Label + 3D Slicer** — AI-assisted annotation workflow

---

## Learning Resources

### Online Courses

1. **AI for Medicine Specialization** — DeepLearning.AI on Coursera
   - URL: https://www.coursera.org/specializations/ai-for-medicine
   - Platform: Coursera | Duration: ~3 months | Cost: Subscription (~$49/month)
   - Covers: Diagnosing diseases from X-rays, 3D MRI brain images, segmentation
   - Difficulty: Intermediate

2. **AI in Healthcare Specialization** — Stanford University on Coursera
   - URL: https://www.coursera.org/specializations/ai-healthcare
   - Platform: Coursera | Duration: ~4 months | Cost: Subscription (~$49/month)
   - Covers: Deep learning for medical imaging, clinical applications, evaluation
   - Difficulty: Intermediate

3. **AI and Machine Learning in MSK Radiology** — Stanford Medicine
   - URL: https://stanford.cloud-cme.com/course/courseoverview?P=8&EID=35549
   - Platform: Stanford CME | Duration: Self-paced | Cost: Free
   - Covers: ML tutorial for radiologists, MSK imaging AI applications
   - Difficulty: Beginner-Intermediate

4. **Medical Image Analysis** — Coursera (offered by various institutions)
   - URL: https://www.coursera.org/learn/medical-image-analysis
   - Platform: Coursera | Duration: ~4 weeks | Cost: Subscription
   - Covers: Image segmentation, registration, classification fundamentals
   - Difficulty: Intermediate

### Video Tutorials and Lectures

5. **Project MONAI YouTube Channel**
   - URL: https://www.youtube.com/@ProjectMONAI/videos
   - Content: Framework overviews, tutorials, deployment guides, community talks
   - Highlight: "Welcome & MONAI Overview" (Nov 2024) — https://www.youtube.com/watch?v=J-GQ1IG1FFY

6. **Introduction to MONAI: Medical Imaging With AI**
   - URL: https://www.youtube.com/watch?v=IP2nghcXJQA
   - Duration: ~30 min | Covers: Core concepts, dataset handling, training, real-world radiology applications

7. **How to use Deep Learning for Medical Imaging using MONAI and PyTorch**
   - URL: https://nourislam.medium.com/how-to-use-deep-learning-for-medical-imaging-using-monai-and-pytorch-8abdb8fc790e
   - Format: Written tutorial with code | Covers: End-to-end MONAI workflow

8. **Integrating AI into Clinical Workflow with Orthanc and OHIF Viewer**
   - URL: https://medium.com/@carlosrl/integrating-ai-into-clinical-workflow-with-orthanc-and-ohif-viewer-27bfc64f2718
   - Format: Written tutorial | Covers: DICOM pipeline integration pattern

### Books

9. **Deep Learning for Medical Image Analysis** — S. Kevin Zhou, Hayit Greenspan, Dinggang Shen (Editors)
   - Publisher: Academic Press | Difficulty: Intermediate-Advanced
   - Covers: Object recognition, segmentation, registration theory and applications
   - Essential reference for medical imaging AI researchers and practitioners

10. **Python for Medical Image Analysis** — Olivier Colliot
    - Practical implementation guide using SimpleITK, PyTorch, and MONAI
    - Covers: 3D volume processing, deep learning model deployment
    - Difficulty: Intermediate

11. **Medical Image Processing: Techniques and Applications** — Isaac N. Bankman
    - Foundational text covering image enhancement, segmentation, registration
    - Covers: Multiple imaging modalities with algorithm explanations
    - Difficulty: Beginner-Intermediate

### Documentation and Reference Materials

12. **DICOM Standard — AI Resources**
    - URL: https://www.dicomstandard.org/ai
    - Covers: DICOM supplements for AI, conformance requirements, AI workflow profiles

13. **FDA AI/ML SaMD Resource Page**
    - URL: https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-aiml-enabled-medical-devices
    - Covers: Regulatory guidance, cleared device list, action plan, PCCP guidance

14. **MONAI Documentation**
    - URL: https://docs.monai.io/
    - Covers: API reference, transforms, architectures, deployment guides

15. **highdicom Documentation**
    - URL: https://highdicom.readthedocs.io/en/latest/
    - Covers: Creating DICOM SEG, SR objects from AI outputs; encoding model results

16. **pydicom Documentation**
    - URL: https://pydicom.github.io/pydicom/stable/
    - Covers: Reading/writing DICOM, pixel data extraction, metadata manipulation

17. **OHIF Viewer Documentation**
    - URL: https://docs.ohif.org/
    - Covers: Web-based viewer setup, DICOM SEG display, integration with PACS

### Interactive Exercises and Practice

18. **MONAI Tutorials (GitHub)**
    - URL: https://github.com/Project-MONAI/tutorials
    - Format: Jupyter notebooks | Covers: Classification, segmentation, registration, deployment
    - Includes: MedNIST classification, spleen CT segmentation, brain tumor segmentation

19. **Kaggle: NIH Chest X-ray Dataset**
    - URL: https://www.kaggle.com/datasets/nih-chest-xrays/data
    - Format: Dataset + community notebooks | Practice: Multi-label classification

20. **Kaggle: Understanding DICOM using pydicom for ML**
    - URL: https://www.kaggle.com/code/aryaangarg01/understanding-dicom-using-pydicom-for-ml
    - Format: Interactive notebook | Covers: DICOM parsing, pixel extraction, preprocessing

21. **Medical Segmentation Decathlon**
    - URL: http://medicaldecathlon.com/
    - Format: 10 segmentation challenges across organs/modalities | Difficulty: Intermediate-Advanced

22. **RSNA AI Challenges**
    - URL: https://www.rsna.org/artificial-intelligence/data
    - Format: Competition-style challenges | Covers: Various radiology AI tasks with labeled datasets

23. **PhysioNet Heart Sound Challenge 2016**
    - URL: https://physionet.org/content/challenge-2016/1.0.0/
    - Format: Dataset + challenge | Covers: Heart sound classification from PCG recordings

### GitHub Repositories and Open-Source Projects

24. **Project-MONAI/MONAI**
    - URL: https://github.com/Project-MONAI/MONAI
    - Stars: 5,800+ | PyTorch-based medical imaging AI framework

25. **Project-MONAI/tutorials**
    - URL: https://github.com/Project-MONAI/tutorials
    - Comprehensive collection of Jupyter notebook tutorials for medical imaging tasks

26. **ImagingDataCommons/highdicom**
    - URL: https://github.com/ImagingDataCommons/highdicom
    - High-level DICOM creation for AI outputs (SEG, SR, parametric maps)

27. **pydicom/pydicom**
    - URL: https://github.com/pydicom/pydicom
    - Stars: 1,900+ | Core Python DICOM library

28. **OHIF/Viewers**
    - URL: https://github.com/OHIF/Viewers
    - Stars: 3,000+ | Open-source web-based medical image viewer

29. **jnkather/HistoGAN and PathML**
    - PathML URL: https://github.com/Dana-Farber-AIMI/pathml
    - Computational pathology toolkit for whole slide image analysis

30. **MIC-DKFZ/nnUNet**
    - URL: https://github.com/MIC-DKFZ/nnUNet
    - Stars: 5,500+ | Self-configuring segmentation method — state of the art for many tasks

31. **NeuroSainteAnne/OrthancAI**
    - URL: https://github.com/NeuroSainteAnne/OrthancAI
    - Reference implementation of Orthanc + AI inference pipeline integration

### Community Resources

32. **r/MachineLearning and r/medicalimaging** — Reddit communities
    - URL: https://www.reddit.com/r/MachineLearning/ and https://www.reddit.com/r/medicalimaging/

33. **MONAI Community** — GitHub Discussions and Slack
    - URL: https://github.com/Project-MONAI/MONAI/discussions

34. **OHIF Community Forum**
    - URL: https://community.ohif.org/

35. **Orthanc Discussion Forum**
    - URL: https://discourse.orthanc-server.org/

---

## Learning Path

### Phase 1: Medical Imaging Foundations (2-3 weeks)

**Cluster 1A: DICOM and Medical Image Data (Week 1)**
- Understand DICOM standard structure (patient → study → series → instance)
- Learn pydicom for reading/writing DICOM files
- Understand imaging modalities and their data characteristics
- Practice: Parse DICOM files, extract pixel data, explore metadata
- Milestone: Can load, manipulate, and visualize DICOM data from multiple modalities

**Cluster 1B: Computer Vision Foundations for Medical Imaging (Week 2-3)**
- CNN architectures review (ResNet, DenseNet, EfficientNet)
- Transfer learning for medical images (ImageNet → medical domain)
- Data augmentation strategies for medical images
- Handling class imbalance in medical datasets
- Practice: Build a chest X-ray classifier using CheXpert or NIH dataset
- Milestone: Can train and evaluate a medical image classifier with proper metrics

### Phase 2: Core Medical Imaging Tasks (3-4 weeks)

**Cluster 2A: Medical Image Segmentation (Week 3-4)**
- U-Net architecture deep dive
- 3D segmentation with V-Net, UNETR
- MONAI framework: transforms, data loading, training loops
- Loss functions: Dice loss, focal loss, boundary loss
- Practice: Complete MONAI spleen segmentation tutorial
- Milestone: Can train a 3D segmentation model using MONAI

**Cluster 2B: Detection and Localization (Week 5)**
- Object detection applied to medical imaging
- Anomaly detection and heatmap generation (GradCAM, attention maps)
- Automated measurement and quantification
- Practice: Build a lung nodule detection pipeline
- Milestone: Can localize and classify abnormalities in medical images

**Cluster 2C: Digital Pathology (Week 6)**
- Whole slide imaging concepts and challenges (gigapixel images)
- Patch-based processing and multiple instance learning
- Tools: QuPath, PathML
- Practice: Process a WSI and build a patch classifier
- Milestone: Understands WSI pipeline from scanning to AI inference

### Phase 3: DICOM Pipeline Integration (2 weeks)

**Cluster 3A: Building the AI Pipeline (Week 7)**
- Set up Orthanc DICOM server
- DICOMweb APIs (WADO-RS, STOW-RS, QIDO-RS)
- AI inference service architecture
- Encoding results with highdicom (DICOM SEG, SR)
- Practice: Build end-to-end pipeline: Orthanc → AI model → results back to PACS
- Milestone: Can deploy an AI model that integrates with a DICOM workflow

**Cluster 3B: Visualization and Clinical Integration (Week 8)**
- OHIF Viewer setup and customization
- Displaying AI results (segmentation overlays, structured reports)
- IHE AI Workflow for Imaging profile
- Practice: Configure OHIF to display AI-generated segmentation results
- Milestone: Can demonstrate AI results in a clinical viewer

### Phase 4: Audio Perception for Healthcare (1-2 weeks)

**Cluster 4A: Clinical Audio Analysis (Week 9)**
- Audio preprocessing: spectrograms, MFCCs, mel features
- Heart sound classification from PCG signals
- Respiratory sound analysis (crackles, wheezes)
- CNN and RNN architectures for audio classification
- Practice: Build heart sound classifier using PhysioNet 2016 data
- Milestone: Can process clinical audio and build classification models

**Cluster 4B: Other Audio Applications (Week 10)**
- Fall detection from ambient audio
- Cough detection and respiratory monitoring
- Clinical conversation analysis basics
- Practice: Build a respiratory sound anomaly detector using ICBHI dataset
- Milestone: Understands audio perception pipeline for clinical deployment

### Phase 5: Regulatory and Deployment (1-2 weeks)

**Cluster 5A: FDA SaMD for Imaging AI (Week 11)**
- SaMD risk classification framework
- 510(k) vs. De Novo pathways
- Predetermined Change Control Plans (PCCP)
- Clinical validation: MRMC studies, standalone performance
- Good Machine Learning Practice (GMLP) principles
- Practice: Draft a regulatory strategy document for a hypothetical imaging AI product
- Milestone: Can articulate the regulatory pathway for an imaging AI product

**Cluster 5B: Specialty Applications (Week 12)**
- Wound assessment AI
- Document OCR for healthcare
- Medication verification from images
- Surgical workflow recognition
- Dermoscopy AI
- Milestone: Broad awareness of computer vision applications beyond radiology

---

## Practical Exercises

### Beginner

1. **DICOM Explorer** — Use pydicom to load chest X-ray DICOM files, extract pixel data, display with matplotlib, read metadata tags (patient name, modality, study description). Convert between DICOM and PNG/NumPy formats.

2. **Chest X-ray Classifier** — Using NIH ChestX-ray14 dataset, build a multi-label classifier for common thoracic diseases. Start with a pre-trained ResNet, apply transfer learning. Evaluate with AUC-ROC per disease.

3. **Audio Feature Extraction** — Load respiratory sound recordings from ICBHI dataset, compute MFCCs and mel spectrograms using librosa, visualize the features, and understand how different respiratory conditions appear in the frequency domain.

### Intermediate

4. **Organ Segmentation with MONAI** — Complete the MONAI spleen segmentation tutorial using CT data from Medical Segmentation Decathlon. Train a 3D U-Net, evaluate with Dice score, visualize predictions with 3D Slicer.

5. **DICOM AI Pipeline** — Set up Orthanc server, build a Python service that: (a) receives DICOM studies, (b) runs a classification model, (c) creates DICOM SR with findings using highdicom, (d) stores results back in Orthanc. View in OHIF.

6. **Heart Sound Classifier** — Using PhysioNet 2016 challenge data, build a CNN classifier on mel spectrograms to distinguish normal vs. abnormal heart sounds. Implement proper cross-validation and report sensitivity/specificity.

7. **Skin Lesion Classification** — Using ISIC Archive data, build a dermoscopy image classifier (melanoma vs. benign). Apply test-time augmentation and ensemble methods. Analyze model errors across skin tones.

### Advanced

8. **End-to-End Radiology AI System** — Build a complete chest X-ray triage system: DICOM ingestion → preprocessing → multi-disease classification → critical finding prioritization → DICOM SR generation → display in OHIF. Include a monitoring dashboard.

9. **Whole Slide Image Pipeline** — Process a CAMELYON16 WSI: tile extraction, patch-level classification, slide-level aggregation using MIL. Implement attention-based MIL for interpretability.

10. **FDA Submission Mock-Up** — For your chest X-ray system, prepare: (a) intended use statement, (b) algorithm description, (c) clinical validation study design (MRMC), (d) PCCP for anticipated model updates, (e) labeling mockup. Use FDA guidance as reference.

11. **Multi-Modal Clinical Perception** — Combine image + audio: build a system that analyzes both chest X-rays and respiratory sounds for respiratory disease assessment. Explore fusion strategies (early, late, attention-based).

---

## Connections to Other Domains

| Domain | Connection |
|--------|-----------|
| D-1: Healthcare Data Foundations | DICOM standard, HIPAA for imaging data, regulatory landscape for SaMD |
| D-2: ML Fundamentals | CNNs, transfer learning, evaluation metrics applied to medical images |
| D-3: Predictive AI | Classification and regression on imaging biomarkers |
| D-4: Foundation Models | Vision transformers, multimodal models (image + text) |
| D-6: Generative AI | Synthetic medical image generation, report generation from images |
| D-8: Fine-Tuning | Domain adaptation for medical imaging models |
| D-9: Clinical Decision Support | Imaging AI outputs feeding CDS systems |
| D-10: AI Safety | Clinical evaluation, bias detection in imaging AI |
| D-11: AI Observability | Monitoring imaging AI in production, drift detection |
| D-12: Agentic Systems | Multimodal perception as agent capability |
| D-13: Capstone | Integrating imaging AI into multi-modal architecture |
