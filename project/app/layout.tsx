import './globals.css';
import type { Metadata } from 'next';
import { Inter, Space_Grotesk, JetBrains_Mono } from 'next/font/google';

const sans = Inter({
  subsets: ['latin'],
  variable: '--font-sans',
  display: 'swap',
});

const display = Space_Grotesk({
  subsets: ['latin'],
  weight: ['500', '700'],
  variable: '--font-display',
  display: 'swap',
});

const mono = JetBrains_Mono({
  subsets: ['latin'],
  variable: '--font-mono',
  display: 'swap',
});

export const metadata: Metadata = {
  title: 'THE ARCHIVE — Digital Dossier Registry',
  description:
    'A cinematic, state-controlled digital archive. A linear, immersive sequence from atmospheric entry through to the character-index registry.',
  openGraph: {
    title: 'THE ARCHIVE — Digital Dossier Registry',
    description:
      'A cinematic, state-controlled digital archive. Scroll to traverse four pinned sections.',
    images: [{ url: 'https://bolt.new/static/og_default.png' }],
  },
  twitter: {
    card: 'summary_large_image',
    images: [{ url: 'https://bolt.new/static/og_default.png' }],
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className={`${sans.variable} ${display.variable} ${mono.variable}`}>
      <body className=" font-sans antialiased">{children}</body>
    </html>
  );
}
