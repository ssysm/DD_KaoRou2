from sys import platform

ffmpegBinDict = {
  'darwin': 'platforms/darwin/ffmpeg/ffmpeg',
  'win32': 'platforms/win32/ffmpeg/ffmpeg.exe'
}

anime4kBinDict = {
  'darwin': '/dev/null',
  'win32': 'platforms/win32/Anime4K/Anime4KCPP_CLI.exe'
}

youtubeDLBinDict = {
  'darwin': 'platforms/darwin/youtube-dl',
  'win32': 'platforms/win32/youtube-dl.exe'
}

binDict = {
  'ffmpeg': ffmpegBinDict,
  'anime4k': anime4kBinDict,
  'youtube-dl': youtubeDLBinDict
}

def getBin(bin_name):
  try:
    got_bin_dict = binDict.get(bin_name)
    return got_bin_dict.get(platform)
  except expression as identifier:
    return None

def getOS():
  return platform