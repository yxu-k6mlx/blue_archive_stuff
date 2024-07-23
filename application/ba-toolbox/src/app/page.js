import Logo from "./logo";
import Directions from "./directions";
import styles from "./page.module.css";
import Footer from "./footer"
import App from "./app" 

export default function Home() {
  return (
    <main className={styles.main}>
      <Logo />
      <Directions />
      <Footer />
    </main>
  );
}
