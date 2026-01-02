// class ApiClient {
//     baseUrl: string;
//
//     constructor(baseUrl: string) {
//         this.baseUrl = baseUrl;
//     }
//
//     async request(path: string, method = "GET", data?: any) {
//         const response = await fetch(
//             `${this.baseUrl}${path}`, {
//                 method,
//                 headers: {
//                     "Content-type": "application/json",
//                 },
//                 body: data ? JSON.stringify(data) : undefined,
//             }
//         );
//
//         if (!response.ok) {
//             const err = await response.json().catch(() => ({}));
//             throw new Error(err.detail || "Request error");
//         }
//
//         return response.json()
//     }
//
//     async authWebApp(initData: string) {
//         return this.request("/auth", "POST", { initData });
//     }
// }
//
// export const api = new ApiClient("/api");