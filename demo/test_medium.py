import torch
from seamless_communication.models.inference import Translator

# Initialize a Translator object with a multitask model, vocoder on the GPU.
translator = Translator("seamlessM4T_medium", vocoder_name_or_card="vocoder_36langs", device=torch.device("cuda:0"))

translated_text, wav, sr = translator.predict("Hey this is a test", "t2st", "eng", src_lang="eng")

wav, sr = translator.synthesize_speech(<speech_units>, <tgt_lang>)

# Save the translated audio generation.
torchaudio.save(
    '/demo',
    wav[0].cpu(),
    sample_rate=sr,
)

