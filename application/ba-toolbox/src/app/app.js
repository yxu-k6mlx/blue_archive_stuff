import Image from "next/image";
import React from 'react'; 

export default function MainApp(){
    return (
        <Image
            src="/ba_toolbox_logo.png"
            alt="Hi :)"
            width={1086}
            height={350}
            priority
            unoptimized={false}
        />
    ); 
}
