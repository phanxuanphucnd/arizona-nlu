[![PyPI - Python](https://img.shields.io/badge/python-3.6%20|%203.7%20|%203.8-blue.svg)](https://github.com/phanxuanphucnd/arizona-nlu)
[![PyPI - License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/phanxuanphucnd/arizona-nlu/blob/main/LICENSE)
[![Open In Jupyter notebook](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/phanxuanphucnd/arizona-nlu/tree/main/tests)

<img src="docs/imgs/arizona_nlu.gif" width="35%" height="35%" align="right" />

## Table of contents

1. [Instroduction](#introduction)
2. [How to use `Arizona-nlu`](#how_to_use)
   - [Installation](#installation)
   - [Data structrue](#data_structure)
   - [Example usage](#usage)
4. [Reference](#reference)

# <a name='introduction'></a> Arizona-nlu

- Nature language understanding (NLU) is a subtopic of natural-language processing in artificial intelligence that deals with machine reading comprehension. Natural-language understanding is considered an AI-hard problem. NLU tasks including two main components: Intent Classification (IC) and Named Entities Recognition (NER).

- `arizona nlu` provide a library for jointly IC and NER tasks based on Transformers architecture.

# <a name='how_to_use'></a> How to use

## <a name='installation'></a> Installation

```js

```

## <a name='data_structure'></a> Data structure

text | intent | tags 
---- | ------ | ---- 
hello you, i need a coffe | demand | O O O O O B-food

## <a name='usage'></a> Example usage

### Training

```py

```

### Evaluation

```py

```

### Inference

```py

```


# <a name='reference'></a> Reference

<a name='paper_1'></a> [1]. Qian Chen, Zhu Zhuo and Wen Wang: “[BERT for Joint Intent Classification and Slot Filling](https://arxiv.org/abs/1902.10909)”, in arXiv:1902.10909, 2019.

# License

      MIT License

      Copyright (c) 2021 Phuc Phan

      Permission is hereby granted, free of charge, to any person obtaining a copy
      of this software and associated documentation files (the "Software"), to deal
      in the Software without restriction, including without limitation the rights
      to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
      copies of the Software, and to permit persons to whom the Software is
      furnished to do so, subject to the following conditions:

      The above copyright notice and this permission notice shall be included in all
      copies or substantial portions of the Software.

      THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
      IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
      FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
      AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
      LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
      OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
      SOFTWARE.

  
# Author

`arizona.nlu` was developed by Phuc Phan © Copyright 2021.

For any questions or comments, please contact the following email: phanxuanphucnd@gmail.com

# Acknowledgement

Our code is based on the unofficial implementation of the [JointBERT+CRF github](https://github.com/monologg/JointBERT) and [paper](https://arxiv.org/abs/1902.10909).