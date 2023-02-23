FROM alleninstitute/bmtk
USER root
RUN /usr/bin/apt update
RUN /usr/bin/apt install -y cmake gcc curl
COPY . .
USER $MAMBA_USER
WORKDIR alleninstitute/bmtk 
RUN python grab_two_image_spikes.py
RUN python applytov1l4.py
