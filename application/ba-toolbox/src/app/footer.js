import styles from "./page.module.css";

export default function Footer() {
    return (
        <div>
            <div className={styles.doublecol}>
                <div>
                    <p>IMPORTANT NOTICES: </p>
                    <p>This site is NOT is not affiliated with Nexon, Nexon Games or Yostar. All game artwork, information and assets used are the property and copyright of the respective authors.</p>
                </div>
                <div>
                    <p>免责声明: </p>
                    <p>本站只是个二创站, 和Nexon, Nexon Games, 或Yostar没有任何正式关联. 所有游戏内图像, 信息, 和内容均为各自的版权方所有. 本站为非商业个人兴趣站, 还请不要过度解读, 谢谢! </p>
                </div>
            </div>
        </div>

    ); 
}