import Image from "next/image";

export default function Logo(){
    return (
        <Image
            src="/ba_toolbox_logo.png"
            alt="Hi :)"
            width={1086}
            height={350}
            priority
            unoptimized={true}
        />
    ); 
}
