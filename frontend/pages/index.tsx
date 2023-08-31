import Image from 'next/image'
import Head from 'next/head'
import { Inter } from 'next/font/google'
import Header from '@/components/Header'
import Banner from '@/components/Banner'

const inter = Inter({ subsets: ['latin'] })

export default function Home() {
  return (
   <div className="relative h-screen bg-gradient-to-b lg:h-[140vh]">
    <Head>
      <title>Home - Netflix</title>
    </Head>
    <Header/>
    <main className="relative pl-4 pb-24 lg:space-y-24 lg:pl-16">

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

// export const getServerSideProps = async () => {
//   const 
// }
