import faster_whisper
import os

print(f"Version: {getattr(faster_whisper, '__version__', 'unknown')}")

try:
    from faster_whisper import BatchedInferencePipeline
    print("BatchedInferencePipeline: YES")
except ImportError:
    print("BatchedInferencePipeline: NO")

try:
    from faster_whisper import decode_audio
    print("decode_audio: YES")
except ImportError:
    print("decode_audio: NO")

try:
    import ffmpeg
    print("ffmpeg-python: YES")
except ImportError:
    print("ffmpeg-python: NO")
