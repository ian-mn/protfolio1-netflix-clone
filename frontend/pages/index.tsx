import Image from 'next/image'
import Head from 'next/head'
import { Inter } from 'next/font/google'
import Header from '@/components/Header'
import Banner from '@/components/Banner'

const inter = Inter({ subsets: ['latin'] })

export default function Home() {
  return (
   <div className="relative h-screen lg:h-[140vh] bg-gradient-to-b from-gray-900/100">
    <Head>
      <title>Home - Netflix</title>
    </Head>
    <Header/>
    <main>

      <Banner/>
      <section>
        {/* Row */}
        {/* Row */}
        {/* Row */}
        {/* Row */}
        {/* Row */}
        {/* Row */}
        {/* Row */}
      </section>
    </main>
    {/* Modal */}

   </div> 
  )
}
