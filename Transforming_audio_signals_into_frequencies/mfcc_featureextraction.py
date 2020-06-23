from python_speech_features import mfcc
import scipy.io.wavfile as wav


def wav_to_mfcc(wav_filename, num_cepstrum):
    """ extract MFCC features from a wav file

    :param wav_filename: filename with .wav format
    :param num_cepstrum: number of cepstrum to return
    :return: MFCC features for wav file
    """
    
    # implement
    rate, data = wav.read(wav_filename)
    mfcc_feature = mfcc(data, rate, numcep=num_cepstrum)
    return mfcc_feature