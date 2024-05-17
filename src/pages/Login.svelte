<script>
  import { getAuth, signInWithPopup, GoogleAuthProvider } from "firebase/auth";
  import { user$ } from "../store";
  const provider = new GoogleAuthProvider();
  const auth = getAuth();
  const loginWithGoogle = async () => {
    const result = await signInWithPopup(auth, provider);
    const credential = GoogleAuthProvider.credentialFromResult(result);
    const token = credential.accessToken;
    const user = result.user;
    user$.set(user);
    localStorage.setItem("token", token);
    try {
    } catch (error) {
      console.error(error);
    }
  };
</script>

<div>
  {#if $user$}
    <div>{JSON.stringify($user$?.displayName)} 로그인 상태입니다.</div>
  {/if}
  <div>로그인 하기</div>
  <button class="login-btn" on:click={loginWithGoogle}>
    <div>Google로 시작하기</div>
  </button>
</div>

<style>
  .login-btn {
    width: 200px;
    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>
