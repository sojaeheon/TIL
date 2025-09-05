// YouTube 검색 함수. 키는 .env에서.
import http from './http'

const YT_BASE = 'https://www.googleapis.com/youtube/v3/search'
const API_KEY = import.meta.env.VITE_YOUTUBE_API_KEY

export async function searchYoutubeVideos(query, maxResults = 6) {
  try {
    const res = await http.get(YT_BASE, {
      params: {
        key: API_KEY,
        part: 'snippet',
        q: query,
        type: 'video',
        maxResults,
        regionCode: 'KR',
        safeSearch: 'strict'
      }
    })
    return res.data.items
  } catch (e) {
    throw new Error('유튜브 영상을 불러오지 못했습니다.')
  }
}
