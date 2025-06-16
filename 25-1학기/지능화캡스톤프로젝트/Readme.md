폴더구조

OpenPCDet/
├── data/
│   └── kitti/                             # 외장하드 경로를 연결한 심볼릭 링크
│       ├── training/
│       │   ├── image_2/
│       │   ├── label_2/
│       │   ├── velodyne/
│       │   └── calib/
│       └── ImageSets/
│           ├── train.txt
│           ├── val.txt
│           └── test.txt
├── tools/
│   └── cfgs/
│       └── kitti_models/
│           └── pointpillar.yaml          # config 수정본
├── requirements.txt                      # 설치 의존성
├── setup.py
├── README.md                             # ⬇ 아래 내용으로 작성
└── ...


# 📦 OpenPCDet KITTI 기반 3D 객체 검출 실험

## 📍 프로젝트 개요
- **목표:** OpenPCDet 프레임워크를 활용한 KITTI 포맷 기반 3D 객체 검출 학습 실험
- **환경:** WSL2 (Ubuntu 20.04) + Python 3.10 + CUDA 11.8 + PyTorch 1.13.1 + OpenPCDet
- **결과:** 데이터 전처리까지 완료, CUDA 및 버전 충돌로 학습 완료에는 실패

---

## 🧰 설치 및 환경 구성

```bash
# 가상환경 생성 및 활성화
python3.10 -m venv openpcdet-env
source openpcdet-env/bin/activate

# 의존성 설치
pip install -r requirements.txt

# OpenPCDet 설치
python setup.py develop


데이터 구성
ln -s /mnt/e/AIHub /home/jinho/OpenPCDet/data/kitti

데이터 전처리
python -m pcdet.datasets.kitti.kitti_dataset


문제 및 한계
PyTorch, CUDA, NumPy, Kornia 간 호환성 문제

pointnet2 CUDA 컴파일 실패 (undefined symbol) 및 Kornia TorchScript 오류

일부 이미지/라벨 누락으로 get_image_shape에서 AssertionError 발생

