import type { Config } from 'tailwindcss';

const config: Config = {
  darkMode: ['class'],
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['var(--font-sans)', 'sans-serif'],
        mono: ['var(--font-mono)', 'monospace'],

          orbitron: ['Orbitron', 'sans-serif'],
          display: ['"Barlow Condensed"', 'sans-serif']
        
      },
      backgroundImage: {
        'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
        'gradient-conic':
          'conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))',
        'grid-faint':
          'linear-gradient(to right, rgba(10,10,10,0.06) 1px, transparent 1px), linear-gradient(to bottom, rgba(10,10,10,0.06) 1px, transparent 1px)',
        'grid-faint-light':
          'linear-gradient(to right, rgba(232,226,212,0.05) 1px, transparent 1px), linear-gradient(to bottom, rgba(232,226,212,0.05) 1px, transparent 1px)',
      },
      borderRadius: {
        lg: 'var(--radius)',
        md: 'calc(var(--radius) - 2px)',
        sm: 'calc(var(--radius) - 4px)',
      },
      colors: {
        background: 'hsl(var(--background))',
        foreground: 'hsl(var(--foreground))',
        card: {
          DEFAULT: 'hsl(var(--card))',
          foreground: 'hsl(var(--card-foreground))',
        },
        popover: {
          DEFAULT: 'hsl(var(--popover))',
          foreground: 'hsl(var(--popover-foreground))',
        },
        primary: {
          DEFAULT: 'hsl(var(--primary))',
          foreground: 'hsl(var(--primary-foreground))',
        },
        secondary: {
          DEFAULT: 'hsl(var(--secondary))',
          foreground: 'hsl(var(--secondary-foreground))',
        },
        muted: {
          DEFAULT: 'hsl(var(--muted))',
          foreground: 'hsl(var(--muted-foreground))',
        },
        accent: {
          DEFAULT: 'hsl(var(--accent))',
          foreground: 'hsl(var(--accent-foreground))',
        },
        destructive: {
          DEFAULT: 'hsl(var(--destructive))',
          foreground: 'hsl(var(--destructive-foreground))',
        },
        border: 'hsl(var(--border))',
        input: 'hsl(var(--input))',
        ring: 'hsl(var(--ring))',
        chart: {
          '1': 'hsl(var(--chart-1))',
          '2': 'hsl(var(--chart-2))',
          '3': 'hsl(var(--chart-3))',
          '4': 'hsl(var(--chart-4))',
          '5': 'hsl(var(--chart-5))',
        },
        // --- Dossier palette (60-30-10 brutalist editorial) ---
        // 60% dominant: paper (warm bone) + ink (near-black)
        paper: {
          DEFAULT: '#E8E2D4',
          dim: '#D8D1BE',
          deep: '#C9C2B0',
        },
        ink: {
          DEFAULT: '#0A0A0A',
          soft: '#161616',
          slate: '#222222',
        },
        // 30% secondary: concrete neutrals
        concrete: {
          DEFAULT: '#6B665C',
          light: '#9A9388',
          dark: '#3A3833',
        },
        bone: '#C9C2B0',
        // 10% accent: signal red + amber (used sparingly)
        signal: {
          DEFAULT: '#D6342C',
          deep: '#A8231C',
          tint: '#E8635A',
        },
        amber: {
          DEFAULT: '#C8862E',
          deep: '#9A661F',
        },
      },
      keyframes: {
        'accordion-down': {
          from: { height: '0' },
          to: { height: 'var(--radix-accordion-content-height)' },
        },
        'accordion-up': {
          from: { height: 'var(--radix-accordion-content-height)' },
          to: { height: '0' },
        },
        'grain-shift': {
          '0%,100%': { transform: 'translate(0,0)' },
          '20%': { transform: 'translate(-4%,3%)' },
          '40%': { transform: 'translate(3%,-5%)' },
          '60%': { transform: 'translate(-3%,4%)' },
          '80%': { transform: 'translate(4%,-2%)' },
        },
        'pulse-slow': {
          '0%,100%': { opacity: '0.4' },
          '50%': { opacity: '1' },
        },
        'scan': {
          '0%': { transform: 'translateY(-100%)' },
          '100%': { transform: 'translateY(100vh)' },
        },
        'blink': {
          '0%,49%': { opacity: '1' },
          '50%,100%': { opacity: '0' },
        },
      },
      animation: {
        'accordion-down': 'accordion-down 0.2s ease-out',
        'accordion-up': 'accordion-up 0.2s ease-out',
        'grain': 'grain-shift 8s steps(5) infinite',
        'pulse-slow': 'pulse-slow 2.4s ease-in-out infinite',
        'scan': 'scan 7s linear infinite',
        'blink': 'blink 1.1s steps(1) infinite',
      },
    },
  },
  plugins: [require('tailwindcss-animate')],
};
export default config;
