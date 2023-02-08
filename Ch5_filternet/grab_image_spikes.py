import os
import matplotlib.pyplot as plt
import numpy as np
from glob import glob
from PIL import Image

#from allensdk.core.brain_observatory_cache import BrainObservatoryCache
from bmtk.simulator import filternet
from bmtk.analyzer.spike_trains import plot_raster

from bmtk.simulator import pointnet

#from bmtk.analyzer.spike_trains import plot_raster
def get_natural_scenes(output_dir='bob_images'):
    """Fetches the 118 Brain Obs natural scene images from the data, saves them in npy format"""
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    boc = BrainObservatoryCache(manifest_file='boc/manifest.json')
    data_set = boc.get_ophys_experiment_data(501498760)
    scenes = data_set.get_stimulus_template('natural_scenes')

    for i in range(0, len(scenes)):
        scene = scenes[i]
        base_name = os.path.join(output_dir, 'scene.{:03d}.gray_{}x{}'.format(i, scene.shape[0], scene.shape[1]))
        plt.imsave('{}.png'.format(base_name), scene, cmap='gray')
        # np.save('{}.npy'.format(base_name), scene)


def create_movie_natural_scenes(images, movie_path, image_dur=1250.0,  gs_dur=500.0, res_row=120, res_col=240, fps=1000.0):
    """Will create a movie of the given images - with a pre- and post- grey-screen of the same duration"""
    frames_per_image = int((image_dur/1000.0)*fps)
    frames_per_gs = int(int((gs_dur/1000.0)*fps))
    n_frames = frames_per_gs + len(images)*frames_per_image + frames_per_gs

    output_mat = np.zeros((n_frames, res_row, res_col), dtype=float)
    c_frame = frames_per_gs
    for img_path in images:
        pic = Image.open(img_path).convert('L')
        pic = pic.resize((res_col, res_row))
        pic_data = np.asarray(pic)
        pic_data = pic_data.astype(dtype=float) * 2.0 / 255.0 - 1.0
        output_mat[c_frame:(c_frame + frames_per_image), :, :] = pic_data

        c_frame += frames_per_image

    movies_dir = os.path.dirname(movie_path)
    if not os.path.exists(movies_dir):
        os.makedirs(movies_dir)
        
    np.save(movie_path, output_mat)


def show_movie(movie_file, frames):
    """Helps visualize the movie"""
    movie_array = np.load(movie_file)
    fig, ax = plt.subplots(1, len(frames), figsize=(40, 5*len(frames)))

    for i, frame in enumerate(frames):
        ax[i].imshow(movie_array[frame, :, :], cmap='gray', vmin=-1.0, vmax=1.0)
        # ax[i].set_xticks([])
        ax[i].set_xticks([0])
        ax[i].set_xticklabels([frame],fontsize=20)

        ax[i].set_yticks([])

    ax[5].set_xlabel('Frame #', horizontalalignment='right', fontsize=20)
    plt.subplots_adjust(wspace=0, hspace=0)

    #plt.show()
    plt.savefig("natural_scenes.png")

if not os.path.exists('bob_images'):
    # Only need to download bob_images once
    get_natural_scenes()
"""
# Fetch 8 images, create a movie of images including beginning and ending grey-screen
images = glob('bob_images/scene*.png')

"""
images = glob('bob_images/scene*.png')
orubt
print(len(images))
images = np.random.choice(images, size=12, replace=False)
print(len(images))

create_movie_natural_scenes(images, movie_path='movies_new/ns_movie.9images.npy')
#size = len(images) * 1000
show_movie(movie_file='movies_new/ns_movie.9images.npy', frames=range(0, 3500, 250))

config = filternet.Config.from_json('config.filternet_ns.json')
config.build_env()

net = filternet.FilterNetwork.from_config(config)
sim = filternet.FilterSimulator.from_config(config, net)
sim.run()



_ = plot_raster(config_file='config.filternet_ns.json', group_by='model_template',save_as="LGN_Spikes_Russell.png")


configure = pointnet.Config.from_json('config.pointnet_ns.json')
configure.build_env()

network = pointnet.PointNetwork.from_config(configure)
sim = pointnet.PointSimulator.from_config(configure, network)
sim.run()



_ = plot_raster(config_file='config.pointnet_ns.json', group_by='model_name', show=False,save_as="Application_of_LGN_Spikes_ontoL4_Russell.png")


def get_touchofevil_movies(output_dir='movies', res_row=120, res_col=240, fps=1000):
    frame_conv = int(np.floor(fps/30.0))
    def convert_movie(name, movie):
        t, x, y = movie.shape
        n_frames = frame_conv * t
        movie_updated = np.zeros((n_frames, res_row, res_col), dtype=float)
        c_frame = 0
        for frame in range(t):
            # Resize resolution
            img = Image.fromarray(movie[frame, :, :], mode='L')
            img = img.resize((res_col, res_row))
            img_data = np.asarray(img)
            img_data = img_data.astype(dtype=float) * 2.0 / 255.0 -1.0

            # Upscale frame rate
            movie_updated[c_frame:(c_frame + frame_conv), :, :] = img_data
            c_frame += frame_conv

        np.save('{}/{}.{}ms.{}x{}.npy'.format(output_dir, name, c_frame, res_row, res_col), movie_updated)

    boc = BrainObservatoryCache(manifest_file='boc/manifest.json')
    data_set = boc.get_ophys_experiment_data(506248008)
    movie = data_set.get_stimulus_template('natural_movie_one')
    convert_movie('natural_movie_one', movie)

    movie = data_set.get_stimulus_template('natural_movie_two')
    convert_movie('natural_movie_two', movie)

#get_touchofevil_movies()