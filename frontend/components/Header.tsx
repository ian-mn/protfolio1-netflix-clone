import Image from 'next/image'
import {MagnifyingGlassIcon, BellIcon} from "@heroicons/react/24/solid"
import Link from 'next/link'
import { useEffect, useState } from 'react'

function Header() {
  const [isScrolled, setIsScrolled] = useState(false)

  useEffect(() => {
    const handleScroll = () => {
      if (window.scrollY > 0) {
        setIsScrolled(true)
      } else {
        setIsScrolled(false)
      }
    }

    window.addEventListener('scroll', handleScroll)

    return () => {
      window.removeEventListener('scroll', handleScroll)
    }
  }, [])

  return (
    <header className={`${isScrolled && 'bg-[#141414]'}`}>

      <div className="flex items-center space-x-2 md:space-x-10">
        <img 
          src="https://rb.gy/ulxxee"
          alt="logo"
          width={100}
          height={100}
          className="cursor-pointer object-contain" 
        />
        <ul className="hidden space-x-4 md:flex">
          <li className="headerLink">Домой</li>
          <li className="headerLink">ТВ-шоу</li>
          <li className="headerLink">Фильмы</li>
          <li className="headerLink">Новое и популярное</li>
          <li className="headerLink">Мой список</li>
        </ul>
      </div>

      <div className="flex items-center space-x-4 text-sm font-light">
        <MagnifyingGlassIcon className="hidden sm:inline h-6 w-6"/>
        <p className="hidden lg:inline">Детям</p>
        <BellIcon className="h-6 w-6"/>
        <Link href="/account">
          <img
            src="https://rb.gy/g1pwyx"
            alt="Account"
            className="cursor-pointer rounded"
          />
        </Link>
      </div>
    </header>
  )
}

export default Header