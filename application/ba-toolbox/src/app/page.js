import Logo from "./logo";
import Directions from "./directions";
import styles from "./page.module.css";

export default function Home() {
  return (
    <main className={styles.main}>
      <Logo />
      <Directions />
    </main>
  );
}
