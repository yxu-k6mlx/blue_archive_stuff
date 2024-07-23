import Image from "next/image";
import styles from "./page.module.css";

export default function Home() {
  return (
    <main className={styles.main}>
      <div className={styles.center}>
        <Image
          src="/ba_toolbox_logo.png"
          alt="Hi :)"
          width={1086}
          height={350}
          priority
          unoptimized={false}
        />
      </div>

      <div className={styles.grid}>
        <a
          href="https://yxu-k6mlx.github.io/"
          className={styles.card}
          target="_blank"
          rel="noopener noreferrer" 
        >
          <h2>
            My Page <br></br>我的主页 <span>-&gt;</span>
          </h2>
          <p>Find out more about me and my contacts. </p>
          <p>点击了解更多关于本站作者的信息和联系方式. </p>
        </a>

        <a
          href="https://yxu-k6mlx.github.io/Experimental/experimental.html"
          className={styles.card}
          target="_blank"
          rel="noopener noreferrer"
        >
          <h2>
            Experiments <br></br>我的试验田 <span>-&gt;</span>
          </h2>
          <p>Visit my other experimental and learning projects here. </p>
          <p>从这里查看我的其他学习成果. </p>
        </a>

        <a
          href="https://github.com/yxu-k6mlx/blue_archive_stuff/tree/main/application/ba-toolbox"
          className={styles.card}
          target="_blank"
          rel="noopener noreferrer"
        >
          <h2>
            GitHub Page <br></br> GitHub主页 <span>-&gt;</span>
          </h2>
          <p>Track progress and contribute to this project. </p>
          <p>
            简体中文的项目相关介绍和内容请点此进入GitHub查看. 
          </p>
        </a>

        <a
          href="https://yxu-k6mlx.github.io/Projects/readme.html"
          className={styles.card}
          target="_blank"
          rel="noopener noreferrer"
        >
          <h2>
            Other Projects <br></br> 其他项目 <span>-&gt;</span>
          </h2>
          <p>See my other projects. </p>
          <p>查看我的其他项目. </p>
        </a>
      </div>
    </main>
  );
}
