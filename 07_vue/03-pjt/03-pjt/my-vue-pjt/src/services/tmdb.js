// TMDB Top Rated/Detail API 함수. 키는 .env에서.
import http from './http'

const TMDB_BASE = 'https://api.themoviedb.org/3'
const API_KEY = import.meta.env.VITE_TMDB_API_KEY

export async function fetchTopRatedMovies(page = 1) {
  try {
    const res = await http.get(`${TMDB_BASE}/movie/top_rated`, {
      params: { api_key: API_KEY, language: 'ko-KR', page }
    })
    return res.data.results
  } catch (e) {
    throw new Error('영화 목록을 불러오지 못했습니다.')
  }
}

export async function fetchMovieDetail(movieId) {
  try {
    const res = await http.get(`${TMDB_BASE}/movie/${movieId}`, {
      params: { api_key: API_KEY, language: 'ko-KR' }
    })
    return res.data
  } catch (e) {
    throw new Error('영화 상세 정보를 불러오지 못했습니다.')
  }
}
