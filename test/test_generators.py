"""Numerically verify generator outputs
"""

import numpy as np
import sys
import os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from sound_field_analysis import gen, io


def test_ideal_wave_open_pressure():
    array_configuration = io.ArrayConfiguration(array_radius=0.5, array_type='open', transducer_type='pressure')
    results_open_pressure = np.array([[3.5449077018, -0.0642580673, 0.0065998911, 0.0205155302, -0.0064606444],
                                      [0.0000000000, -0.0047384232 + 0.0030425066j, -0.0274719035 + 0.0176395064j, 0.0055649133 - 0.0035731897j, 0.0128614005 - 0.0082582103j],
                                      [0.0000000000, 0.0000000000 + 0.0051133718j, 0.0000000000 + 0.0296457389j, 0.0000000000 - 0.0060052616j, 0.0000000000 - 0.0138791155j],
                                      [0.0000000000, 0.0047384232 + 0.0030425066j, 0.0274719035 + 0.0176395064j, -0.0055649133 - 0.0035731897j, -0.0128614005 - 0.0082582103j]])
    np.testing.assert_allclose(gen.ideal_wave(order=1, azimuth=1, colatitude=1, fs=48000, NFFT=8, array_configuration=array_configuration, wavetype='plane', delay=0, c=343, distance=1), results_open_pressure)


def test_ideal_wave_open_velocity():
    array_configuration = io.ArrayConfiguration(array_radius=0.5, array_type='open', transducer_type='velocity')
    results_open_velocity = np.array([[1.7724538509, -0.0321290337 + 0.0027319952j, 0.0032999455 + 0.0158392581j, 0.0102577651 - 0.0032085181j, -0.0032303222 - 0.0074153959j],
                                      [0.3289843794 + 0.5123628138j, -0.0203150233 - 0.0264276926j, -0.0120591719 + 0.011431183j, 0.0085159795 + 0.0071428379j, 0.0046695870 - 0.0068718764j],
                                      [0.5529057800, -0.0301605294 + 0.0025566859j, 0.0028180708 + 0.0148228695j, 0.0096360135 - 0.0030026308j, -0.0029598052 - 0.0069395577j],
                                      [0.3289843794 - 0.5123628138j, -0.0155766001 + 0.0294701991j, 0.0154127316 + 0.0062083233j, 0.0029510662 - 0.0107160276j, -0.0081918134 - 0.0013863338j]])
    np.testing.assert_allclose(gen.ideal_wave(order=1, azimuth=1, colatitude=1, fs=48000, NFFT=8, array_configuration=array_configuration, wavetype='plane', delay=0, c=343, distance=1), results_open_velocity)


def test_ideal_wave_rigid_pressure():
    array_configuration = io.ArrayConfiguration(array_radius=0.5, array_type='rigid', transducer_type='pressure', scatter_radius=0.5)
    results_rigid_pressure = np.array([[-0.0643576059 + 0.0054621765j, -0.0643576059 + 0.0054621765j, +0.0063112724 + 0.0316758864j, 0.0205545085 - 0.0064167993j, -0.0063930795 - 0.0148304841j],
                                       [-0.0396107140 - 0.0535098563j, -0.0396107140 - 0.0535098563j, -0.0241659405 + 0.0228929274j, 0.0169234688 + 0.0143553364j, +0.0093641662 - 0.0137598001j],
                                       [-0.0603210321 + 0.0040133970j, -0.0603210321 + 0.0040133970j, +0.0056361414 + 0.0296971018j, 0.0192720269 - 0.0058881867j, -0.0059196103 - 0.0139060852j],
                                       [-0.0321725013 + 0.0582858777j, -0.0321725013 + 0.0582858777j, +0.0308730596 + 0.0124472082j, 0.0060106225 - 0.0213623945j, -0.0164086190 - 0.0027887150j]])
    np.testing.assert_allclose(gen.ideal_wave(order=1, azimuth=1, colatitude=1, fs=48000, NFFT=8, array_configuration=array_configuration, wavetype='plane', delay=0, c=343, distance=1), results_rigid_pressure)


def test_ideal_wave_rigid_velocity():
    array_configuration = io.ArrayConfiguration(array_radius=0.5, array_type='rigid', transducer_type='velocity', scatter_radius=0.5)
    results_rigid_velocity = np.array([[-0.0643576059 + 0.0054621765j, -0.0643576059 + 0.0054621765j, +0.0063112724 + 0.0316758864j, 0.0205545085 - 0.0064167993j, -0.0063930795 - 0.0148304841j],
                                       [-0.0396107140 - 0.0535098563j, -0.0396107140 - 0.0535098563j, -0.0241659405 + 0.0228929274j, 0.0169234688 + 0.0143553364j, +0.0093641662 - 0.0137598001j],
                                       [-0.0603210321 + 0.0040133970j, -0.0603210321 + 0.0040133970j, +0.0056361414 + 0.0296971018j, 0.0192720269 - 0.0058881867j, -0.0059196103 - 0.0139060852j],
                                       [-0.0321725013 + 0.0582858777j, -0.0321725013 + 0.0582858777j, +0.0308730596 + 0.0124472082j, 0.0060106225 - 0.0213623945j, -0.0164086190 - 0.0027887150j]])
    np.testing.assert_allclose(gen.ideal_wave(order=1, azimuth=1, colatitude=1, fs=48000, NFFT=8, array_configuration=array_configuration, wavetype='plane', delay=0, c=343, distance=1), results_rigid_velocity)


def test_sampled_wave_open_pressure():
    array_configuration = io.ArrayConfiguration(array_radius=0.1, array_type='open', transducer_type='pressure')
    results_open_pressure = np.array([[1, 1, 1, 1, 1],
                                      [1, -0.79091116 - 0.611930993j, 0.25108092 + 0.967966100j, 0.39374575 - 0.919219387j, -0.87391674 + 0.486075639j],
                                      [1, 1, 1, 1, 1],
                                      [1, 1, 1, 1, 1],
                                      [1, -0.79091116 + 0.611930993j, 0.25108092 - 0.967966100j, 0.39374575 + 0.919219387j, -0.87391674 - 0.486075639j],
                                      [1, 1, 1, 1, 1]])

    np.testing.assert_allclose(gen.sampled_wave(fs=44100, NFFT=8, array_configuration=array_configuration, gridData=gen.lebedev(1), wave_azimuth=0, wave_colatitude=1.570796327), results_open_pressure)


def test_sampled_wave_open_velocity():
    array_configuration = io.ArrayConfiguration(array_radius=0.03, array_type='open', transducer_type='velocity')
    results_open_velocity = np.array([[0.77015115 + 0.00000000e+00j, -0.04895562 + 7.68593615e-01j, -0.76392730 - 9.77132270e-02j, +0.14607561 - 7.56171089e-01j, +0.74535644 + 1.93846973e-01j],
                                      [0.91863357 - 1.31828622e-18j, -0.75354851 + 5.25406767e-01j, +0.31762729 - 8.61974789e-01j, +0.23245375 + 8.88736680e-01j, -0.69898766 - 5.96073772e-01j],
                                      [0.22984885 + 0.00000000e+00j, -0.01461063 - 2.29384006e-01j, -0.22799136 + 2.91621618e-02j, +0.04359574 + 2.25676547e-01j, +0.22244901 - 5.78531609e-02j],
                                      [0.54200346 + 1.13629010e-17j, +0.52459703 + 1.36256052e-01j, +0.47349574 + 2.63760381e-01j, +0.39198183 + 3.74323387e-01j, +0.28529096 + 4.60843475e-01j],
                                      [0.08136643 + 1.31828622e-18j, -0.06674430 - 4.65370261e-02j, +0.02813331 + 7.63479760e-02j, +0.02058920 - 7.87183656e-02j, -0.06191165 + 5.27963484e-02j],
                                      [0.45799654 - 1.13629010e-17j, +0.44328798 - 1.15137272e-01j, +0.40010706 - 2.22879280e-01j, +0.33122726 - 3.16305758e-01j, +0.24107284 - 3.89416026e-01j]])

    np.testing.assert_allclose(gen.sampled_wave(fs=44100, NFFT=8, array_configuration=array_configuration, gridData=gen.lebedev(1), wave_azimuth=0.1, wave_colatitude=1), results_open_velocity)


def test_sampled_wave_rigid_pressure():
    array_configuration = io.ArrayConfiguration(array_radius=0.02, array_type='rigid', transducer_type='pressure', scatter_radius=0.02)
    results_rigid_pressure = np.array([[+0.32054372 + 1.38399959j, +0.32054372 + 1.38399959j, -1.19397035 + 1.10006162j, -1.62310090 - 0.50737109j, -0.33358792 - 1.71688940j],
                                       [-0.61651852 + 1.44795046j, -0.61651852 + 1.44795046j, -1.60768249 - 0.74044015j, +0.90889648 - 1.62077354j, +1.55970182 + 1.07254709j],
                                       [+0.25652813 - 0.72185863j, +0.25652813 - 0.72185863j, -0.70564806 - 0.45545839j, -0.70254800 + 0.42884861j, +0.14535957 + 0.71147564j],
                                       [+1.14780424 - 0.01961643j, +1.14780424 - 0.01961643j, +1.17250448 - 0.28217918j, +1.11023102 - 0.51649741j, +0.99922121 - 0.72057850j],
                                       [-0.66621222 - 0.41340554j, -0.66621222 - 0.41340554j, -0.17237646 + 0.48574798j, +0.61680889 - 0.19378656j, -0.37012158 - 0.25611854j],
                                       [+1.16121830 + 0.42126229j, +1.16121830 + 0.42126229j, +1.16966306 + 0.60757734j, +1.09224217 + 0.80027296j, +0.96642622 + 0.98365721j]])

    np.testing.assert_allclose(gen.sampled_wave(fs=44100, NFFT=8, array_configuration=array_configuration, gridData=gen.lebedev(1), wave_azimuth=-0.1, wave_colatitude=1), results_rigid_pressure)


def test_sampled_wave_rigid_velocity():
    array_configuration = io.ArrayConfiguration(array_radius=0.09, array_type='rigid', transducer_type='velocity', scatter_radius=0.09)
    results_rigid_velocity = np.array([[-0.46438706 + 0.71957504j, -0.46438706 + 0.71957504j, -0.20840478 - 0.74767951j, +0.64478748 + 0.31114761j, -0.61393218 + 0.23623316j],
                                       [-0.87370712 + 1.72087709j, -0.87370712 + 1.72087709j, -1.41022794 - 1.38345843j, +1.78373160 - 0.87835591j, +0.22133665 + 1.98053786j],
                                       [-1.18800718 - 1.20601922j, -1.18800718 - 1.20601922j, +0.31716851 + 1.75993533j, +0.77912649 - 1.66287130j, -1.62959038 + 0.91152068j],
                                       [+0.82835116 + 1.14446552j, +0.82835116 + 1.14446552j, -0.25442440 + 1.44231619j, -1.24695382 + 0.81968782j, -1.46942234 - 0.35546783j],
                                       [+0.12237009 + 0.48998046j, +0.12237009 + 0.48998046j, -0.23995081 - 0.06586052j, +0.18914288 - 0.10894187j, +0.01577603 + 0.19703264j],
                                       [+0.84655643 - 0.86099104j, +0.84655643 - 0.86099104j, -0.09828927 - 1.21951868j, -0.97850185 - 0.72568973j, -1.18338227 + 0.24200079j]])

    np.testing.assert_allclose(gen.sampled_wave(fs=44100, NFFT=8, array_configuration=array_configuration, gridData=gen.lebedev(1), wave_azimuth=0.1, wave_colatitude=2), results_rigid_velocity)
