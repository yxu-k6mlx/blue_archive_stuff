import Image from "next/image";
import styles from "./page.module.css";

export default function Home_zh() {
  return (
    <main className={styles.main}>
      <div className={styles.center}>
        <Image
          className={styles.title}
          src="/ba_toolbox_logo.png"
          alt="Hi :)"
          width={1086}
          height={350}
          priority
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
            My Page <span>-&gt;</span>
          </h2>
          <p>Find out more about me and my contacts. </p>
        </a>

        <a
          href="https://github.com/yxu-k6mlx/blue_archive_stuff/"
          className={styles.card}
          target="_blank"
          rel="noopener noreferrer"
        >
          <h2>
            GitHub Page <span>-&gt;</span>
          </h2>
          <p>Track progress and contribute to this project. </p>
        </a>

        <a
          href="https://yxu-k6mlx.github.io/Projects/readme.html"
          className={styles.card}
          target="_blank"
          rel="noopener noreferrer"
        >
          <h2>
            Other Projects <span>-&gt;</span>
          </h2>
          <p>See my other projects. </p>
        </a>

        <a
          href=""
          className={styles.card}
          target="_blank"
          rel="noopener noreferrer"
        >
          <h2>
            简体中文站 <span>-&gt;</span>
          </h2>
          <p>
            施工中.
          </p>
        </a>
      </div>
    </main>
  );
}
