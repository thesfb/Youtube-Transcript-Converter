import re
from youtube_transcript_api import YouTubeTranscriptApi

def cleaned_link(link):
  if bool(re.search(r'v=', link)) == True:
    return link[32:43]
  elif bool(re.search(r'.be/', link)) == True:
    return link[17:28]

def get_trans(clean_link):
  trans_list = []
  try:
    trans_raw = YouTubeTranscriptApi.get_transcript(clean_link)
  except Exception as e:
    print('Subtitle not Found!!')
  else:
    for ele in trans_raw:
      trans_list.append(ele['text'])
      
  return trans_list

    
  