FROM python:3
WORKDIR /data/NAPSTER_LABS/PROJECTS/PYTHON/youtube-music
COPY . .
CMD ["music.py"]
ENTRYPOINT ["python3"]
