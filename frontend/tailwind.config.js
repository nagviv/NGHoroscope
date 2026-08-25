/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        vedic: {
          gold: '#D4AF37',
          maroon: '#800020',
          dark: '#0F172A',
          card: '#1E293B',
          accent: '#F59E0B'
        }
      }
    },
  },
  plugins: [],
}
