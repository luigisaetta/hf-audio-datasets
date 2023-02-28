import soundfile as sf
import torchaudio
from tqdm import tqdm


def check_channels(f_name, n_channels):
    v_rit = True

    vet, s_rate = sf.read(f_name)

    try:
        if vet.shape[1] != n_channels:
            v_rit = False
    except:
        # if mono it is a one dimensional array OK
        v_rit = True

    return v_rit


def check_max_length(f_name, max_length):
    v_rit = True

    vet, s_rate = sf.read(f_name)

    duration = vet.shape[0] / s_rate

    if duration > max_length:
        print(f"Duration : {round(duration, 1)} s.")
        v_rit = False

    return v_rit


def check_sampling_rate(f_name, sampling_rate):
    """
    return true if the sample_rate is the expected
    """
    vet, s_rate = sf.read(f_name)

    v_rit = True

    if s_rate != sampling_rate:
        v_rit = False

    return v_rit


# for audio augmentation
# from https://jonathanbgn.com/2021/08/30/audio-augmentation.html


class AudioSpeedChanger:
    def __init__(self, sample_rate):
        self.sample_rate = sample_rate

    def __call__(self, audio_data, speed_factor):
        # limits what could be done
        assert speed_factor in [0.9, 1.0, 1.1]

        if speed_factor == 1.0:  # no change
            return audio_data

        # change speed and resample to original rate:
        sox_effects = [
            ["speed", str(speed_factor)],
            ["rate", str(self.sample_rate)],
        ]
        transformed_audio, _ = torchaudio.sox_effects.apply_effects_tensor(
            audio_data, self.sample_rate, sox_effects
        )

        return transformed_audio


def compute_duration_min(ds, sampling_rate):
    """
    Input is train or test HF dataset
    """
    tot_duration_secs = 0

    for row in tqdm(ds["audio"]):
        row_audio = row["array"]

        duration = row_audio.shape[0] / sampling_rate

        tot_duration_secs += duration

    tot_duration_min = tot_duration_secs / 60.0

    return round(tot_duration_min, 1)
