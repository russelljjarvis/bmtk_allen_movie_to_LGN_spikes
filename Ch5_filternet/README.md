```
git clone https://github.com/russelljjarvis/bmtk_workshop_2022
docker pull alleninstitute/bmtk
sudo docker run -v `pwd`:/home/shared/workspace alleninstitute/bmtk python grab_two_image_spikes.py
```