// 공통 axios 인스턴스. TMDB/YouTube API용.
import axios from 'axios'

const http = axios.create({
  timeout: 7000,
})

export default http
