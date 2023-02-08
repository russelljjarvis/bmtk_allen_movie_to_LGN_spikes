This is a repository for converting movies of static scenes into realistic spikes that would run through LGN On/Off cel

* First make sure Docker is installed.

* We can use the `alleninstitute/bmtk` docker version of `bmtk` and `allensdk`, this is because those packages now have painful dependencies.

* Edit the file grab_two_image_spikes.py to get the number of naturalistic scenes to use.

The scenes picked are a random choice, try hardcoding in specific file names. See a list of all files below (these will populate a directory called bob_images).

* To convert a movie to LGN spikes, where the movie is sourced from two random static naturalistic scenes.
```
git clone https://github.com/russelljjarvis/bmtk_allen_movie_to_LGN_spikes
cd bmtk_allen_movie_to_LGN_spikes/Ch5_filternet
docker pull alleninstitute/bmtk
sudo docker run -v `pwd`:/home/shared/workspace alleninstitute/bmtk python grab_two_image_spikes.py
sudo docker run -v `pwd`:/home/shared/workspace alleninstitute/bmtk python applytov1l4.py
```

To increase the cell count of population sizes of simulated LGN and L4 edit build_network_greater_cell_count.py

and then re-run. Presumably this will increase the representation in the LGN:
```
sudo docker run -v `pwd`:/home/shared/workspace alleninstitute/bmtk python build_network_greater_cell_count.py
```

This will change json configuration files that are used as arguments in the Python files below.

```
sudo docker run -v `pwd`:/home/shared/workspace alleninstitute/bmtk python grab_two_image_spikes.py
sudo docker run -v `pwd`:/home/shared/workspace alleninstitute/bmtk python applytov1l4.py

```

![https://github.com/russelljjarvis/bmtk_allen_movie_to_LGN_spikes/blob/develop/Ch5_filternet/LGN_Spikes_png.png](https://github.com/russelljjarvis/bmtk_allen_movie_to_LGN_spikes/blob/develop/Ch5_filternet/LGN_Spikes_png.png)
![https://github.com/russelljjarvis/bmtk_allen_movie_to_LGN_spikes/blob/develop/Ch5_filternet/natural_scenes.png](https://github.com/russelljjarvis/bmtk_allen_movie_to_LGN_spikes/blob/develop/Ch5_filternet/natural_scenes.png)
![https://github.com/russelljjarvis/bmtk_allen_movie_to_LGN_spikes/blob/develop/Ch5_filternet/Application_of_LGN_Spikes_ontoL4.png](https://github.com/russelljjarvis/bmtk_allen_movie_to_LGN_spikes/blob/develop/Ch5_filternet/Application_of_LGN_Spikes_ontoL4.png)




bmtk_workshop_2022/Ch5_filternet/bob_images/$ ls
```
scene.000.gray_918x1174.png  scene.015.gray_918x1174.png  scene.030.gray_918x1174.png  scene.045.gray_918x1174.png  scene.060.gray_918x1174.png  scene.075.gray_918x1174.png  scene.090.gray_918x1174.png  scene.105.gray_918x1174.png
scene.001.gray_918x1174.png  scene.016.gray_918x1174.png  scene.031.gray_918x1174.png  scene.046.gray_918x1174.png  scene.061.gray_918x1174.png  scene.076.gray_918x1174.png  scene.091.gray_918x1174.png  scene.106.gray_918x1174.png
scene.002.gray_918x1174.png  scene.017.gray_918x1174.png  scene.032.gray_918x1174.png  scene.047.gray_918x1174.png  scene.062.gray_918x1174.png  scene.077.gray_918x1174.png  scene.092.gray_918x1174.png  scene.107.gray_918x1174.png
scene.003.gray_918x1174.png  scene.018.gray_918x1174.png  scene.033.gray_918x1174.png  scene.048.gray_918x1174.png  scene.063.gray_918x1174.png  scene.078.gray_918x1174.png  scene.093.gray_918x1174.png  scene.108.gray_918x1174.png
scene.004.gray_918x1174.png  scene.019.gray_918x1174.png  scene.034.gray_918x1174.png  scene.049.gray_918x1174.png  scene.064.gray_918x1174.png  scene.079.gray_918x1174.png  scene.094.gray_918x1174.png  scene.109.gray_918x1174.png
scene.005.gray_918x1174.png  scene.020.gray_918x1174.png  scene.035.gray_918x1174.png  scene.050.gray_918x1174.png  scene.065.gray_918x1174.png  scene.080.gray_918x1174.png  scene.095.gray_918x1174.png  scene.110.gray_918x1174.png
scene.006.gray_918x1174.png  scene.021.gray_918x1174.png  scene.036.gray_918x1174.png  scene.051.gray_918x1174.png  scene.066.gray_918x1174.png  scene.081.gray_918x1174.png  scene.096.gray_918x1174.png  scene.111.gray_918x1174.png
scene.007.gray_918x1174.png  scene.022.gray_918x1174.png  scene.037.gray_918x1174.png  scene.052.gray_918x1174.png  scene.067.gray_918x1174.png  scene.082.gray_918x1174.png  scene.097.gray_918x1174.png  scene.112.gray_918x1174.png
scene.008.gray_918x1174.png  scene.023.gray_918x1174.png  scene.038.gray_918x1174.png  scene.053.gray_918x1174.png  scene.068.gray_918x1174.png  scene.083.gray_918x1174.png  scene.098.gray_918x1174.png  scene.113.gray_918x1174.png
scene.009.gray_918x1174.png  scene.024.gray_918x1174.png  scene.039.gray_918x1174.png  scene.054.gray_918x1174.png  scene.069.gray_918x1174.png  scene.084.gray_918x1174.png  scene.099.gray_918x1174.png  scene.114.gray_918x1174.png
scene.010.gray_918x1174.png  scene.025.gray_918x1174.png  scene.040.gray_918x1174.png  scene.055.gray_918x1174.png  scene.070.gray_918x1174.png  scene.085.gray_918x1174.png  scene.100.gray_918x1174.png  scene.115.gray_918x1174.png
scene.011.gray_918x1174.png  scene.026.gray_918x1174.png  scene.041.gray_918x1174.png  scene.056.gray_918x1174.png  scene.071.gray_918x1174.png  scene.086.gray_918x1174.png  scene.101.gray_918x1174.png  scene.116.gray_918x1174.png
scene.012.gray_918x1174.png  scene.027.gray_918x1174.png  scene.042.gray_918x1174.png  scene.057.gray_918x1174.png  scene.072.gray_918x1174.png  scene.087.gray_918x1174.png  scene.102.gray_918x1174.png  scene.117.gray_918x1174.png
scene.013.gray_918x1174.png  scene.028.gray_918x1174.png  scene.043.gray_918x1174.png  scene.058.gray_918x1174.png  scene.073.gray_918x1174.png  scene.088.gray_918x1174.png  scene.103.gray_918x1174.png
scene.014.gray_918x1174.png  scene.029.gray_918x1174.png  scene.044.gray_918x1174.png  scene.059.gray_918x1174.png  scene.074.gray_918x1174.png  scene.089.gray_918x1174.png  scene.104.gray_918x1174.png
```
