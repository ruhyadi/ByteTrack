
### Download Model
```
gdown https://drive.google.com/uc?id=1uSmhXzyV1Zvb4TJJCzpsZOIcw7CCJLxj
```

```bash
python tools/demo_track.py video \
    --path demo/demo.mp4 \
    -f exps/example/mot/yolox_s_mix_det.py \
    -c pretrained/bytetrack_s_mot17.pth.tar \
    --fp16 --fuse --save_result
```