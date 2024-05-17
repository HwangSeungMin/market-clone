<script>
  import Footer from "../components/Footer.svelte";
  import { user$ } from "../store";

  const logout = () => {
    user$.set(null);
    localStorage.removeItem("token");
    window.location.hash = "/";
  };
</script>

<div>나의 당근</div>
<button on:click={logout}>Log-out</button>
<Footer location="my" />
