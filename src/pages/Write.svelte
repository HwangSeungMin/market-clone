<script>
  import Footer from "../components/Footer.svelte";
  import { getDatabase, ref, push } from "firebase/database";
  import {
    getStorage,
    ref as refImage,
    uploadBytes,
    getDownloadURL,
  } from "firebase/storage";

  let title;
  let price;
  let description;
  let place;
  let files;

  const storage = getStorage();
  const db = getDatabase();

  async function writeUserData(imgUrl) {
    push(ref(db, "items/"), {
      title: title,
      price: price,
      description: description,
      place: place,
      insertAt: new Date().getTime(),
      imgUrl,
    });
    window.location.hash = "/";
  }

  const uploadFiles = async () => {
    const file = files[0];
    const name = file.name;
    const blob = new Blob([file], { type: file.type });
    const imgRef = refImage(storage, name);
    await uploadBytes(imgRef, blob);
    const url = await getDownloadURL(imgRef);
    return url;
  };

  const handleSubmit = async () => {
    const url = await uploadFiles();
    writeUserData(url);
  };
</script>

<form id="write-form" on:submit|preventDefault={handleSubmit}>
  <div>
    <label for="image">이미지</label>
    <input type="file" id="image" name="image" bind:files />
  </div>
  <div>
    <label for="title">제목</label>
    <input type="text" id="title" name="title" bind:value={title} />
  </div>
  <div>
    <label for="price">가격</label>
    <input type="number" id="price" name="price" bind:value={price} />
  </div>
  <div>
    <label for="description">설명</label>
    <input
      type="text"
      id="description"
      name="description"
      bind:value={description}
    />
  </div>
  <div>
    <label for="place">장소</label>
    <input type="text" id="place" name="place" bind:value={place} />
  </div>
  <div>
    <button class="write-button" type="submit">글쓰기 완료!</button>
  </div>
</form>

<Footer location="write" />

<style>
  .write-button {
    background-color: azure;
    border: 1px solid grey;
    margin: 5px;
    border-radius: 3px;
  }
</style>
