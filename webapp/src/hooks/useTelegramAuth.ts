import {useCallback, useEffect, useState} from "react";
import type {ApiClient} from "../shared/api/http.ts";

export interface User {
    id: number;
    username: string;
    balance: number;
    is_admin: boolean;
    discount: number;
    photo_url: string;
    bot_username: string;
}


export function useTelegramAuth(api: ApiClient) {
    const [user, setUser] = useState<User | null>(null);
    const [error, setError] = useState<string | null>(null);
    const [loading, setLoading] = useState(true);

    const fetchUser = useCallback(async () => {
        try {
            setLoading(true);

            const tg = (window as any).Telegram.WebApp;
            const initData = tg?.initData;

            if (!initData) {
                setError("No init data provided!");
                return;
            }

            const response = await api.authWebApp(initData);
            setUser(response);
            setError(null);
        } catch (e: any) {
            setError(e.message || "Unknown error");
        } finally {
            setLoading(false);
        }
    }, [api]);

    useEffect(() => {
        fetchUser();
    }, [fetchUser]);

    return {
        user,
        loading,
        error,
        refetch: fetchUser,
    };
}