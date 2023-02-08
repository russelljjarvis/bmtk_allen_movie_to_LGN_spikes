
First make sure Docker is installed.
To create a movie of two static naturalistic scenes, and to convert the movie to spikes use:
```
git clone https://github.com/russelljjarvis/bmtk_allen_movie_to_LGN_spikes
cd bmtk_allen_movie_to_LGN_spikes/Ch5_filternet
docker pull alleninstitute/bmtk
sudo docker run -v `pwd`:/home/shared/workspace alleninstitute/bmtk python grab_two_image_spikes.py
```