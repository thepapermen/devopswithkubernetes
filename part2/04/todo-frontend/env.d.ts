/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_API_ROOT_URL: string;
  readonly VITE_IMAGE_BACKEND_URL: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}
