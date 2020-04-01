from datetime import datetime, date, timedelta
import click
from model import Word, Review


@click.group()
def cli():
    pass


@cli.command()
@click.pass_context
def learn(ctx):
    words = Word.select().where((Word.stage == 0) & (Word.next_review == datetime.today()))
    if not len(words):
        click.echo(f"Your day is clear!")
        return

    for index, word in enumerate(words):
        click.echo(f"{index+1}/{len(words)} {word.en} {word.ch}")
        click.echo("now input this word three times!")
        correct_time = 0
        while correct_time < 3:
            if click.prompt("") == word.en:
                correct_time += 1
                click.echo(f"correct! {correct_time} count!")
            else:
                click.echo(f"Try Again!")
        click.echo("Good work!\n")

    click.echo("You've learned all the words!\n"
               "Now It's time to check how you remember them!\n"
               "Let's go to our first review process!\n")
    ctx.invoke(review, words)


@cli.command()
@click.pass_context
def review(ctx, words):
    for index, word in enumerate(words):
        click.echo(f"{index+1}/{len(words)} {word.en} {word.ch}")
        click.echo(f"{word.ch}")
        error_count = 0
        while click.prompt("") != word.en:
            error_count += 1
            click.prompt("not correct! try again!")

        new_review = Review.create()
        new_review.word_id = word.id
        new_review.review_at = datetime.now()
        new_review.stage_before = word.stage
        word.stage += (not error_count)
        new_review.stage_after = word.stage
        new_review.error_count = error_count
        word.save()
        new_review.save()

        if not error_count:
            click.echo(f"correct! the stage of word `{word.en}` has changed from "
                       f"stage {new_review.stage_before} to stage {new_review.stage_after}!\n")
        else:
            click.echo(f"Oops! due to the error_count {error_count},"
                       f"you're still in stage{word.stage} for word `{word}`!"
                       f"Try to do better at next time!\n")

        click.echo("Congrats! You've finished all the review tasks\n!")


if __name__ == '__main__':
    cli()
