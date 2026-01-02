import axios, {type AxiosInstance, type AxiosRequestConfig } from 'axios'
import type {User} from "../../hooks/useTelegramAuth.ts";


export class ApiClient {
  private client: AxiosInstance

  constructor(baseURL: string) {
    this.client = axios.create({
      baseURL,
      headers: {
        'Content-Type': 'application/json',
      },
      timeout: 10_000,
    })
  }

    private async request<T>(config: AxiosRequestConfig): Promise<T> {
      try {
      const response = await this.client.request<T>(config)
      return response.data
    } catch (error: any) {
      const message =
        error?.response?.data?.detail ||
        error?.response?.data?.message ||
        error?.message ||
        'Request error'

      throw new Error(message)
    }
  }

  authWebApp(initData: string):Promise<User> {
    return this.request<User>({
      url: '/auth',
      method: 'POST',
      data: { initData },
    })
  }
}

export const api = new ApiClient('/api')
