import torch
from seamless_communication.models.inference import Translator
import torchaudio

# Initialize a Translator object with a multitask model, vocoder on the GPU.
translator = Translator("seamlessM4T_medium", vocoder_name_or_card="vocoder_36langs", device=torch.device("cuda:0"))

translated_text, wav, sr = translator.predict("Hey this is a test", "t2st", "eng", src_lang="eng")

#wav, sr = translator.synthesize_speech("Hey this is a test", "eng")

# Save the translated audio generation.
torchaudio.save(
    '/root/sushant/seamless_m4t/seamless_communication/demo/output.wav',
    wav[0].cpu(),
    sample_rate=sr,
)


