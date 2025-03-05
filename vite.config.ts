import { fileURLToPath, URL } from 'url';
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import vuetify from 'vite-plugin-vuetify';

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [
        vue(),
        vuetify({
            autoImport: true,
            styles: { configFile: 'src/scss/variables.scss' }
        })
    ],
    resolve: {
        alias: {
            '@': fileURLToPath(new URL('./src', import.meta.url))
        }
    },
    css: {
        preprocessorOptions: {
            scss: {}
        }
    },
    optimizeDeps: {
        exclude: ['vuetify'],
        entries: ['./src/**/*.vue']
    },
    // build: {
    //     rollupOptions: {
    //         treeshake:  false 
    //     }
    // },
    server: { 
        proxy: {
            '/api': {
                target: 'http://127.0.0.1:5000', // URL de tu backend (¡Verifica que sea la correcta!)
                changeOrigin: true,
                // rewrite: (path) => path.replace(/^\/api/, ''), // Opcional: Elimina /api del path si es necesario
            },
        },
    },
});
