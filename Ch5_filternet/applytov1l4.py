import os
import matplotlib.pyplot as plt
import numpy as np
from glob import glob
from PIL import Image

#from allensdk.core.brain_observatory_cache import BrainObservatoryCache
from bmtk.simulator import filternet
from bmtk.analyzer.spike_trains import plot_raster

from bmtk.simulator import pointnet

configure = pointnet.Config.from_json('config.pointnet_ns.json')
configure.build_env()

network = pointnet.PointNetwork.from_config(configure)
sim = pointnet.PointSimulator.from_config(configure, network)
sim.run()



_ = plot_raster(config_file='config.pointnet_ns.json', group_by='model_name', show=False,save_as="Application_of_LGN_Spikes_ontoL4.png")
