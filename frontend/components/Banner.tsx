import React from 'react'
import Image from 'next/image'
import {FaPlay} from 'react-icons/fa'
import {InformationCircleIcon} from "@heroicons/react/24/solid"


function Banner() {
  return (
    <div className="flex flex-col space-y-2 py-16 md:space-y-4 lg:h-[65vh] lg:justify-end lg:pb-12">
      <div className="absolute top-0 left-0 -z-10 h-[95vh] w-screen">
        <Image
          src="https://imagetmdb.com/t/p/original/7RyHsO4yDXtBv1zUU3mTpHeQ0d5.jpg"
          alt="Banner"
          fill={true}
          objectFit="cover"
        />
      </div>

      <h1 className="text-shadow-xl drop-shadow-lg shadow-black text-2xl z-10 lg:text-7xl md:text-4xl">Мстители: Финал</h1>
      <p className="text-shadow-xl max-w-xs z-10 text-xs md:max-w-lg md:text-lg lg:max-w-2xl lg:text-2xl">Оставшиеся в живых члены команды Мстителей и их союзники должны разработать новый план, который поможет противостоять разрушительным действиям могущественного титана Таноса. После наиболее масштабной и трагической битвы в истории они не могут допустить ошибку.</p>
    
    <div className="flex space-x-3">
      <button className="bannerButton bg-white text-black"> 
        <FaPlay className="h-4 w-4 text-black md:h-7 md:w-7"/> Смотреть
      </button>
      <button className="bannerButton bg-[grey]/70">Подробнее <InformationCircleIcon className="h-5 w-5 md:h-8 md:w-8"/></button>
    </div>
    
    </div>
  )
}

export default Banner