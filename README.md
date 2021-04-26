## youtube-summarization

### [Step1] Download Youtube Video to Local

```python
python download_video.py --video_list_path {} --video_path {}
```

### [Step2] Extract video script via Clova Speech API

```python
python clovaspeech_script.py --video_path {} --label_path {}
```